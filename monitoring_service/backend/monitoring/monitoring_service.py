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
from flask import Flask, Response, request, jsonify, send_from_directory
import config
import constants
import datetime
import threading
import json
import logging
from flask_sslify import SSLify
from flask_cors import CORS
from marshmallow import ValidationError

app = Flask(__name__)
CORS(app)
sslify = SSLify(app)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_PATH'] = '/usr/app/images/'
app.config['VIDEO_PATH'] = '/usr/app/test/resources'
app.config['supports_credentials'] = True
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
count = 0
listOfMsgs = []
listOfCameras = []
listOfVideos = []
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4'}


class VideoCamera(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self._person_timeout_check()

    def delete(self):
        self.video.release()

    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        return success, image

    def _person_timeout_check(self):
        threading.Timer(constants.WAIT_SECONDS, self._person_timeout_check).start()
        # logger.debug("Timeout processing")
        now = time.time()
        for msg in listOfMsgs:
            if now - msg["time"] > constants.PERSON_TIMEOUT_SECONDS:
                listOfMsgs.remove(msg)


class VideoFile(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, video_name):
        self.video = cv2.VideoCapture("/usr/app/test/resources/" + video_name)
        self._person_timeout_check()

    def delete(self):
        self.video.release()

    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        return success, image

    def _person_timeout_check(self):
        threading.Timer(constants.WAIT_SECONDS, self._person_timeout_check).start()
        # logger.debug("Timeout processing")
        now = time.time()
        for msg in listOfMsgs:
            if now - msg["time"] > constants.PERSON_TIMEOUT_SECONDS:
                listOfMsgs.remove(msg)


def allowed_file(filename):
    """
    File types to upload:png, jpg, jpeg
    param: filename:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_videofile(filename):
    """
    File types to upload:mp4
    param: filename:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


def send_notification_msg(camera_name, name):
    global count

    url = constants.frontend_url + "/notify"
    camera = camera_name.split("-")
    if name != "unknown":
        if len(listOfMsgs) == 0:
            count = count + 1
            newdict = {"msgid": count, "time": time.time(), "relatedObj": name,
                       "msg": name + " has appeared in front of camera " + camera[0]}

            listOfMsgs.append(newdict)
            person_info = newdict.copy()
            person_info["time"] = datetime.datetime.fromtimestamp(newdict["time"]).strftime("%Y%m%d-%H:%M:%S")
            requests.post(url, json=person_info)
        flag = False
        for msg in listOfMsgs:
            if name in msg.values():
                flag = True
                break
        if not flag:
            count = count + 1
            newdict = {"msgid": count, "time": time.time(), "relatedObj": name,
                       "msg": name + " has appeared in front of camera " + camera[0]}
            listOfMsgs.append(newdict)
            person_info = newdict.copy()
            person_info["time"] = datetime.datetime.fromtimestamp(newdict["time"]).strftime("%Y%m%d-%H:%M:%S")
            requests.post(url, json=person_info)


def video(video_capture, camera_name):
    """
    人脸识别
    """
    process_this_frame = 0
    while True:
        success, frame = video_capture.get_frame()
        if not success:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        data = ""
        # Convert the image from BGR color  to RGB color
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame == 0:
            url = constants.recognition_url + "/v1/face-recognition/recognition"
            info1 = cv2.imencode(".jpg", rgb_small_frame)[1].tobytes()
            if constants.access_token_enabled and constants.ssl_enabled:
                access_token = get_access_token()
                headers = {'Content-Type': 'application/json', 'Authorization': access_token}
                data = json.loads(requests.post(url, data=info1, headers=headers, verify=config.ssl_cacertpath).text)
            else:
                data = json.loads(requests.post(url, data=info1).text)

        for info in data:
            name = info['Name']
            send_notification_msg(camera_name, name)

        ret, jpeg = cv2.imencode('.jpg', frame)
        process_this_frame = process_this_frame + 1
        if process_this_frame == 2:
            process_this_frame = 0
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/v1/monitor/video', methods=['POST'])
def upload_video():
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if 'file' in request.files:
        files = request.files.getlist("file")
        for file in files:
            if allowed_videofile(file.filename):
                file.save(os.path.join(app.config['VIDEO_PATH'], file.filename))
            else:
                raise IOError('video format error')
    return Response("success")


@app.route('/v1/monitor/cameras', methods=['POST'])
def add_camera():
    camera_info = request.json
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(camera_info["name"]) >= 64 or len(camera_info["location"]) >= 64:
        raise ValidationError("length of the camera name or location is larger than max size")

    camera_info = {"name": camera_info["name"], "rtspurl": camera_info["rtspurl"], "location": camera_info["location"]}
    listOfCameras.append(camera_info)
    return Response("success")


@app.route('/v1/monitor/cameras/<name>/<rtspurl>/<location>', methods=['GET'])
def get_camera(name, rtspurl, location):
    """
    通过摄像头人脸识别
    """
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(name) >= 64 or len(location) >= 64:
        raise ValidationError(constants.person_maxsize)

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
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(camera_name) >= 64:
        raise ValidationError("length of the camera name is larger than max size")

    for video1 in listOfVideos:
        if camera_name in video1:
            video_obj = video1[camera_name]
            video_obj.delete()
    for camera in listOfCameras:
        if camera_name == camera["name"]:
            listOfCameras.remove(camera)
    time.sleep(1)
    camera = camera_name.split("-")
    for msg in listOfMsgs:
        if camera[0] in msg["msg"]:
            listOfMsgs.remove(msg)
    return Response("success")


@app.route('/v1/monitor/cameras')
def query_cameras():
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    return jsonify(listOfCameras)


@app.route('/', methods=['GET'])
def hello_world():
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    return Response("Hello MEC Developer")


@app.route('/v1/monitor/persons', methods=['POST'])
def upload():
    """
    图像录入
    """
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if 'file' not in request.files:
        raise IOError('No file')
    url = constants.recognition_url + "/v1/face-recognition/upload"

    files = request.files.getlist("file")
    for file in files:
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
        else:
            raise IOError('picture format is error')

    upload_files = []
    result = ""
    for file in files:
        upload_files.append(('file', open(os.path.join(app.config['UPLOAD_PATH'], file.filename), 'rb')))

        if constants.access_token_enabled and constants.ssl_enabled:
            access_token = get_access_token()
            headers = {'Content-Type': 'application/json', 'Authorization': access_token}
            result = requests.post(url, files=upload_files, headers = headers, verify=config.ssl_cacertpath)
        else:
            result = requests.post(url, files=upload_files)

    return result.text


@app.route('/v1/monitor/<person_name>')
def monitor_person(person_name):
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.person_maxsize)

    if path.exists(app.config['UPLOAD_PATH'] + person_name):
        return send_from_directory(app.config['UPLOAD_PATH'], person_name)
    else:
        return Response("Image " + person_name + " doesn't exist")


@app.route('/v1/monitor/persons')
def monitor_persons():
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    url = constants.frontend_url + "/uploadFile"
    upload_files = []
    for root, dirs, files in os.walk(app.config['UPLOAD_PATH']):
        for file in files:
            upload_files.append(('file', open(os.path.join(app.config['UPLOAD_PATH'], file), 'rb')))
    requests.post(url, files=upload_files)
    return Response("upload success")


@app.route('/v1/monitor/persons/<person_name>', methods=['DELETE'])
def delete_person(person_name):
    """
    param: person_name
    """
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.person_maxsize)

    person = person_name
    person_name = person_name[0:-4]
    url = constants.recognition_url + "/v1/face-recognition/{0}".format(person_name)

    if constants.access_token_enabled and constants.ssl_enabled:
        access_token = get_access_token()
        headers = {'Content-Type': 'application/json', 'Authorization': access_token}
        result = requests.delete(url, data=person_name, headers = headers, verify=config.ssl_cacertpath)
    else:
        result = requests.delete(url, data=person_name)

    if result:
        os.remove(app.config['UPLOAD_PATH'] + person)
        time.sleep(1)
        for msg in listOfMsgs:
            if person_name in msg["relatedObj"]:
                listOfMsgs.remove(msg)
        return jsonify({'Result': 'delete success'})
    else:
        return jsonify({"Result": "the name is not exist"})


@app.route('/v1/monitor/messages')
def monitor_messages():
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    list_of_msgs = []
    for msg in listOfMsgs:
        person_info = msg.copy()
        person_info["time"] = datetime.datetime.fromtimestamp(person_info["time"]).strftime("%Y%m%d-%H:%M:%S")
        list_of_msgs.append(person_info)
    return jsonify(list_of_msgs)


@app.route('/v1/monitor/persons/<person_name>/messages')
def query_person(person_name):
    app.logger.info(constants.received_message + request.remote_addr + constants.operation + request.method + "]" +
                    constants.resource + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.person_maxsize)

    for msg in listOfMsgs:
        if msg["relatedObj"] == person_name:
            return jsonify(msg)
    return Response("person name " + person_name + " doesn't exist")


def get_access_token():
    url = constants.mep_agent + "/mep-agent/v1/token"
    headers = {'Content-Type': 'application/json'}
    if config.ssl_enabled:
        result = requests.get(url, headers=headers, verify=config.ssl_cacertpath)
    else:
        result = requests.get(url, headers=headers)
    # extracting data in json format
    data = result.json()
    access_token = data["access_token"]
    return access_token


def start_server(handler):
    logging.basicConfig(level=logging.INFO)
    app.logger.addHandler(handler)
    if config.ssl_enabled:
        context = (config.ssl_certfilepath, config.ssl_keyfilepath)
        app.run(host=config.server_address, debug=True, ssl_context=context, threaded=True, port=config.server_port)
    else:
        app.run(host=config.server_address, debug=True, threaded=True, port=config.server_port)