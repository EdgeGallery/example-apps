#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Huawei Technologies Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This is an app application for face recognition microservices.
Its functions are: face upload, face recognition, Video face recognition, etc.
The restfull api is http://127.0.0.1:9999. Database is redis, used to store
the feature vector of the face.
Store face images in data volume postgres
"""
import io
from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from app.face_service import face_upload, face_find, face_compare, face_delete, refresh_redis, web_video, take_photo, \
    camera

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources=r'/*')

# Face Entry Page
@app.route('/v1/face-recognition/upload', methods=['GET'])
def html():
    """
    人脸录入界面
    """
    return '''
    <!doctype html>
    <title>Face entry</title>
    <h1>Face entry</h1>
    <form method="POST" action="/v1/face-recognition/upload" enctype="multipart/form-data">
      <input type="file" name="file" multiple="multiple">
      <input type="submit" value="submit">
    </form>
    '''


# Call cameraPOST
@app.route('/v1/face-recognition/camera', methods=['POST'])
def camera_post():
    """
    拍照
    """

    data = request.get_json()
    url = data["url"]
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"
    response = Response(camera(path),
                      mimetype='multipart/x-mixed-replace; boundary=frame')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'

    return response


# Call camera
@app.route('/v1/face-recognition/camera', methods=['GET'])
def camera_get():
    """
    拍照
    """
    url = request.args['url']
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"

    return Response(camera(path),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


# Face collection
@app.route('/v1/face-recognition/collection', methods=['GET'])
def collection():
    """
    拍照
    """
    url = request.args['url']
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"
    image = take_photo(path)
    response1 = make_response(image.tobytes())
    response1.headers['Content-Type'] = 'images/png'
    return response1


# Face collection
@app.route('/v1/face-recognition/collection', methods=['POST'])
def collection_post():
    """
    拍照
    """
    data = request.get_json()
    url = data["url"]
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"
    image = take_photo(path)
    response1 = make_response(image.tobytes())
    response1.headers['Content-Type'] = 'images/png'
    return response1


@app.route('/v1/face-recognition/upload', methods=['POST'])
def upload():
    """
    图像录入
    """
    if 'file' not in request.files:
        raise IOError('No file')
    files = request.files.getlist("file")
    num = 0
    for file_image in files:
        img = file_image.read()
        face_upload(img, file_image)
        num = num + 1
    return jsonify({'Face number': num, 'Result': 'upload success'})


@app.route('/v1/face-recognition/comparison', methods=['POST'])
def compare_images():
    """
    人脸对比
    """
    if 'file1' not in request.files:
        raise IOError('No file1')
    if 'file2' not in request.files:
        raise IOError('No file2')
    file1 = request.files.get("file1")
    file2 = request.files.get("file2")
    result = face_compare(file1, file2)
    return jsonify(result)


@app.route('/v1/face-recognition/recognition', methods=['POST'])
def search_images():
    """
    人脸识别
    """
    if 'file' in request.files:
        image_file = request.files['file']
        find_faces = face_find(image_file)
        return jsonify(find_faces)
    else:
        file_image = request.get_data()
        find_faces = face_find(io.BytesIO(file_image))
        return jsonify(find_faces)


@app.route('/v1/face-recognition/video', methods=['GET'])
def video_feed1():
    """
    视频监控
    param camera_url:
    """
    url = request.args['url']
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"
    # video_capture = cv2.VideoCapture(path)
    # _, frame = video_capture.read()
    # video_capture.release()
    # if frame is None:
    #     return make_response(jsonify({'result': 'camera url is error'}), 403)
    return Response(web_video(path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/v1/face-recognition/video', methods=['POST'])
def video_feed():
    """
    视频监控
    param camera_url:
    """
    data = request.get_json()
    url = data["url"]
    if url == '0':
        path = int(url)
    else:
        path = "rtsp://admin:HuaWei123@" + url + ":554/LiveMedia/Ch1/Media1"
    return Response(web_video(path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/v1/face-recognition/refresh', methods=['POST'])
def update_redis():
    """
    刷新redis，将postgres数据库中的人脸图片生成特征向量并导入redis数据库
    """
    name = refresh_redis()
    return jsonify({'Face name in redis': str(name), 'Result': 'refresh success'})


@app.route('/v1/face-recognition/<name>', methods=['DELETE'])
def delete_images(name):
    """
    删除人脸， 将postgres数据库以及redis中人脸信息删除
    param: name
    """
    result = face_delete(name)
    if result:
        return jsonify({'Result': 'delete success'})
    else:
        return jsonify({"Result": "the name is not exist"})


@app.route('/v1/face-recognition/', methods=['GET'])
def tests():
    """
    test
    """
    return '1'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=True, port=9999)
