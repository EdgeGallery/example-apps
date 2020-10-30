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

import cv2
import requests
import os
import time
from os import path
from flask import Flask, Response, request, jsonify, send_from_directory, send_file
import config
import logging
from flask_sslify import SSLify
from flask_cors import CORS


class VideoCamera(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, url):
        self.video = cv2.VideoCapture(url)

    def delete(self):
        self.video.release()

    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        return success, image


class VideoFile(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, video_name):
        self.video = cv2.VideoCapture("./test/resources/" + video_name)

    def delete(self):
        self.video.release()

    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        return success, image


app = Flask(__name__)
CORS(app)
sslify = SSLify(app)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_PATH'] = '/usr/app/images/'
app.config['supports_credentials'] = True
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
count = 0
listOfMsgs = []
listOfCameras = []
listOfVideos = []


def video(video_capture, camera_name):
    """
    人脸识别
    """
    global count
    process_this_frame = 0
    while True:
        success, frame = video_capture.get_frame()
        if not success:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # Convert the image from BGR color  to RGB color
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame == 0:
            url = config.recognition_url + "/v1/face-recognition/recognition"
            info1 = cv2.imencode(".jpg", rgb_small_frame)[1].tobytes()
            data = json.loads(requests.post(url, data=info1, verify=config.ssl_cacertpath).text)

        for info in data:
            top = info['Face position']['top']
            right = info['Face position']['right']
            bottom = info['Face position']['bottom']
            left = info['Face position']['left']
            name = info['Name']
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)
            if name != "unknown":
                if len(listOfMsgs) == 0:
                    count = count + 1
                    newdict = {"msgid": count, "time": time.strftime("%Y%m%d-%H:%M:%S:" + "321"), "relatedObj": name,
                           "msg": name + " has arrived in front of camera " + camera_name}
                    listOfMsgs.append(newdict)
                flag = False
                for msg in listOfMsgs:
                    if name in msg.values():
                        flag = True
                        break
                if not flag:
                    count = count + 1
                    newdict = {"msgid": count, "time": time.strftime("%Y%m%d-%H:%M:%S:" + "321"), "relatedObj": name,
                           "msg": name + " has arrived in front of camera " + camera_name}
                    listOfMsgs.append(newdict)
        ret, jpeg = cv2.imencode('.jpg', frame)
        process_this_frame = process_this_frame + 1
        if process_this_frame == 2:
            process_this_frame = 0
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/v1/monitor/cameras', methods=['POST'])
def add_camera():
    camera_info = request.json
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    camera_info = {"name": camera_info["name"], "rtspurl": camera_info["rtspurl"], "location": camera_info["location"]}
    listOfCameras.append(camera_info)
    return Response("success")


@app.route('/v1/monitor/cameras/<name>/<rtspurl>/<location>', methods=['GET'])
def get_camera(name, rtspurl, location):
    """
    通过摄像头人脸识别
    """
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    camera_info = {"name": name, "rtspurl": rtspurl, "location": location}
    if "mp4" in camera_info["rtspurl"]:
        video_file = VideoFile(camera_info["rtspurl"])
        video_dict = {camera_info["name"]:video_file}
        listOfVideos.append(video_dict)
        return Response(video(video_file, camera_info["name"]),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        video_file = VideoCamera(camera_info["rtspurl"])
        video_dict = {camera_info["name"]: video_file}
        listOfVideos.append(video_dict)
        return Response(video(video_file, camera_info["name"]),
                     mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/v1/monitor/cameras/<camera_name>', methods=['DELETE'])
def delete_camera(camera_name):
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    for video1 in listOfVideos:
        if camera_name in video1:
            video_obj = video1[camera_name]
            video_obj.delete()
    for camera in listOfCameras:
        if camera_name == camera["name"]:
            listOfCameras.remove(camera)
    for msg in listOfMsgs:
        if camera_name in msg["msg"]:
            listOfMsgs.remove(msg)
    return Response("success")


@app.route('/v1/monitor/cameras')
def query_cameras():
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    return jsonify(listOfCameras)


@app.route('/', methods=['GET'])
def hello_world():
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    return Response("Hello MEC Developer")


@app.route('/v1/monitor/persons', methods=['POST'])
def upload():
    """
    图像录入
    """
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    if 'file' not in request.files:
        raise IOError('No file')
    url = config.recognition_url + "/v1/face-recognition/upload"

    files = request.files.getlist("file")
    for file in files:
        file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))

    upload_files = []
    for file in files:
        upload_files.append(('file', open(os.path.join(app.config['UPLOAD_PATH'], file.filename), 'rb')))

    result = requests.post(url, files=upload_files, verify=config.ssl_cacertpath)
    return result.text


@app.route('/v1/monitor/<person_name>')
def monitor_person(person_name):
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    if path.exists(app.config['UPLOAD_PATH'] + person_name):
        return send_from_directory(app.config['UPLOAD_PATH'], person_name)
    else:
        return Response("Image " + person_name + " doesn't exist")




@app.route('/v1/monitor/persons/<person_name>', methods=['DELETE'])
def delete_person(person_name):
    """
    param: person_name
    """
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    person = person_name
    person_name = person_name[0:-4]
    url = config.recognition_url + "/v1/face-recognition/{0}".format(person_name)

    result = requests.delete(url, data=person_name, verify=config.ssl_cacertpath)
    if result:
        os.remove(app.config['UPLOAD_PATH'] + person)
        for msg in listOfMsgs:
            if person_name in msg["relatedObj"]:
                listOfMsgs.remove(msg)
        return jsonify({'Result': 'delete success'})
    else:
        return jsonify({"Result": "the name is not exist"})


@app.route('/v1/monitor/messages')
def monitor_messages():
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    return jsonify(listOfMsgs)


@app.route('/v1/monitor/persons/<person_name>/messages')
def query_person(person_name):
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    for msg in listOfMsgs:
        if msg["relatedObj"] == person_name:
            return jsonify(msg)
    return Response("person name " + person_name + " doesn't exist")


def start_server(handler):
    app.logger.addHandler(handler)
    if config.ssl_enabled:
        context = (config.ssl_certfilepath, config.ssl_keyfilepath)
        app.run(host=config.server_address, debug=True, ssl_context=context, threaded=True, port=config.server_port)
    else:
        app.run(host=config.server_address, debug=True, threaded=True, port=config.server_port)