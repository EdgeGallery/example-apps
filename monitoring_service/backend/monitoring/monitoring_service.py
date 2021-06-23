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
Exposed an API's of monitoring service
"""
import os
import time
from os import path
import datetime
import threading
import json
import logging
from wsgiref.util import FileWrapper
import cv2
import requests
from flask import Flask, Response, request, jsonify, send_from_directory
from flask_sslify import SSLify
from flask_cors import CORS
from marshmallow import ValidationError
import config
import constants
import clientsdk
import queue

app = Flask(__name__)
CORS(app)
sslify = SSLify(app)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_PATH'] = '/usr/app/images/'
app.config['VIDEO_PATH'] = '/usr/app/test/resources'
app.config['supports_credentials'] = True
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
COUNT = 0
NOW = 0.0
listOfMsgs = []
listOfCameras = []
listOfVideos = []
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4'}
listOfServices = ["face-recognition"]


class VideoCamera(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, url, camera_name):
        if url == "0":
            url = int(url)
        self.stop = False
        self.url = url
        self.camera_name = camera_name
        self.video = cv2.VideoCapture(url)

    def delete(self):
        self.stoped()
        self.video.release()
    
    def isStoped(self):
        return self.stop
    
    def stoped(self):
        self.stop = True


    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        if not success and not self.stop:
            self.video.release()
            self.video = cv2.VideoCapture(self.url)
            success, image = self.video.read
            app.logger.info('==>reinit:'+self.url+'==>'+str(len(listOfVideos))+','+str(success))
        return success, image

    def reset_frame(self):
        """
        获取实时视频流
        """
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)


class VideoFile(object):
    """
    通过opencv获取实时视频流
    """
    def __init__(self, video_name):
        self.stop = False
        self.video_name = video_name
        self.url = "/usr/app/test/resources/" + video_name
        self.video = cv2.VideoCapture(self.url)

    def delete(self):
        self.stoped()
        self.video.release()
        
    def isStoped(self):
        return self.stop
    
    def stoped(self):
        self.stop = True

    def get_frame(self):
        """
        获取实时视频流
        """
        success, image = self.video.read()
        if not success:
            app.logger.info('==>Video read not success,Thread count and listOfVideos count=>'+self.url+','+str(len(threading.enumerate()))+','+str(len(listOfVideos)))
        return success, image

    def reset_frame(self):
        """
        获取实时视频流
        """
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)


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


def process_notification_msg(name, camera, url):
    """
        This method is to process the notification messages
    """
    global COUNT
    flag = False
    cam_flag = False

    for msg in listOfMsgs:
        if name not in msg.values():
            continue
        if name in msg.values() and NOW - msg["time"] > 15:
            flag = True
            break
        message = msg["msg"]
        words = message.split()
        cam = words[-1]
        if name in msg.values() and NOW - msg["time"] < 15 and camera[0] != cam:
            flag = True
            cam_flag = True
            break
        if name in msg.values() and NOW - msg["time"] < 15:
            break

    if flag and cam_flag:
        COUNT = COUNT + 1
        newdict = {"msgid": COUNT, "time": time.time(), "relatedObj": name, "cam_flag": "enable",
                   "msg": name + constants.FRONT_OF_CAMERA + camera[0]}
        listOfMsgs.insert(0, newdict)
        requests.post(url, json=newdict)
    elif flag:
        COUNT = COUNT + 1
        newdict = {"msgid": COUNT, "time": time.time(), "relatedObj": name, "cam_flag": "disable",
                   "msg": name + constants.FRONT_OF_CAMERA + camera[0]}
        listOfMsgs.insert(0, newdict)
        requests.post(url, json=newdict)


def send_notification_msg(camera_name, name):
    """
        This method is to send notification message
    """
    global NOW
    global COUNT

    url = constants.FRONTEND_URL + "/notify"
    camera = camera_name.split("-")
    if name != "unknown":
        if len(listOfMsgs) >= 100:
            listOfMsgs.pop()
        if len(listOfMsgs) == 0:
            COUNT = COUNT + 1
            newdict = {"msgid": COUNT, "time": time.time(), "relatedObj": name,
                       "cam_flag": "disable",
                       "msg": name + constants.FRONT_OF_CAMERA + camera[0]}
            listOfMsgs.insert(0, newdict)
            requests.post(url, json=newdict)
        NOW = time.time()

        person_flag = False
        for msg in listOfMsgs:
            if name in msg.values():
                person_flag = True
                break

        if not person_flag:
            COUNT = COUNT + 1
            newdict = {"msgid": COUNT, "time": time.time(), "relatedObj": name,
                       "cam_flag": "enable",
                       "msg": name + constants.FRONT_OF_CAMERA + camera[0]}
            listOfMsgs.insert(0, newdict)
            requests.post(url, json=newdict)

        process_notification_msg(name, camera, url)


class RecognitionThread(threading.Thread):
    def __init__(self, name, video):
        threading.Thread.__init__(self, name = name)
        self.video = video
        self.queue = queue.Queue()
        self.camera_name = name
        
    def putFrame(self, frame):
        self.queue.put(frame)
    
    def deleteListOfVideos(self):
        for video in listOfVideos:
            if self.camera_name in video:
                video_obj = video[self.camera_name]
                if video_obj is self.video:
                    # video_obj.delete()
                    app.logger.info('listOfVideos remover.before:' + str(len(listOfVideos)))
                    listOfVideos.remove(video_obj)
                    app.logger.info('listOfVideos remover.after:' + str(len(listOfVideos)))
                    break
                
        self.video.delete()
    
    def run(self):
        app.logger.info("Thread starting")
        while True:
            try:
                frame = self.queue.get(timeout=10)
            except Exception:
                self.video.stoped()
                self.deleteListOfVideos()
                app.logger.info("Timeout exceptin thread exit:" + self.name)
            else:
                small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                # Convert the image from BGR color  to RGB color            
                rgb_small_frame = small_frame[:, :, ::-1]
                body = cv2.imencode(".jpg", rgb_small_frame)[1].tobytes()
                rest_client = CLIENT_FACTORY.get_client_by_service_name(constants.FACE_RECOGNITION_SERVICE)
                url = rest_client.get_endpoint() + "/v1/face-recognition/recognition"
                app.logger.info(url)
                response = rest_client.post(url, body)
                app.logger.info("face-recognition response:" + response.text)
                data = json.loads(response.text)
                app.logger.info(response.text)
                for info in data:
                  name = info['Name']
                  app.logger.info("face_name:" + name)
                  send_notification_msg(self.camera_name, name)


def camera_video(video_capture, camera_name):
    """
    人脸识别
    """
    app.logger.info("camera video")
    process_this_frame = 0
    thread = RecognitionThread(name = camera_name, video = video_capture)
    thread.start()
    while True:
        success, frame = video_capture.get_frame()
        if not success:
            app.logger.info('====>camera:' + camera_name + ',not success read frame.')
            break
        if process_this_frame == 0:
            if thread.is_alive():
                thread.putFrame(frame)

        process_this_frame = process_this_frame + 1
        if process_this_frame == 42:
            process_this_frame = 0

        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def video(video_capture, camera_name):
    """
    人脸识别
    """
    app.logger.info("local video")
    process_this_frame = 0
    count = 0
    thread = RecognitionThread(name = camera_name, video = video_capture)
    thread.start()    
    while True:
        success, frame = video_capture.get_frame()
        if count == 5:
            break
        if not success:
            video_capture.reset_frame()
            count = count + 1
            continue
        if process_this_frame == 0:
            if thread.is_alive():
                thread.putFrame(frame)

        count = 0
        process_this_frame = process_this_frame + 1
        if process_this_frame == 21:
            process_this_frame = 0

        _, jpeg = cv2.imencode('.jpg', frame)
        time.sleep(.01)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/v1/monitor/video', methods=['POST'])
def upload_video():
    """
        This method is used to upload a video
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
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
    """
        This method is used to add camera information
    """
    camera_info = request.json
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    if len(camera_info["name"]) >= 64 or len(camera_info["location"]) >= 64:
        raise ValidationError("length of the camera name or location is larger than max size")

    camera_info = {"name": camera_info["name"], "rtspurl": camera_info["rtspurl"],
                   "location": camera_info["location"]}
    listOfCameras.append(camera_info)
    return Response("success")


@app.route('/v1/monitor/cameras/<camera_name>', methods=['GET'])
def get_camera(camera_name):
    """
    通过摄像头人脸识别
    """
    camera_info = {}
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    if len(camera_name) >= 64:
        raise ValidationError(constants.PERSON_MAXSIZE)

    for camera_msg in listOfCameras:
        if camera_name == camera_msg["name"]:
            camera_info = camera_msg
            break

    if "mp4" in camera_info["rtspurl"]:
        video_file = VideoFile(camera_info["rtspurl"])
        video_dict = {camera_info["name"]: video_file}
        listOfVideos.append(video_dict)
        return Response(video(video_file, camera_info["name"]),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        video_file = VideoCamera(camera_info["rtspurl"], camera_name)
        video_dict = {camera_info["name"]: video_file}
        listOfVideos.append(video_dict)
        return Response(camera_video(video_file, camera_info["name"]), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/v1/monitor/cameras/<camera_name>', methods=['DELETE'])
def delete_camera(camera_name):
    """
        This method is used to delete camera information
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
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
    for msg in reversed(range(len(listOfMsgs))):
        if camera[0] in listOfMsgs[msg]['msg']:
            del listOfMsgs[msg]
    return Response("success")


@app.route('/v1/monitor/cameras')
def query_cameras():
    """
        This method is used to query camera information
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    return jsonify(listOfCameras)


@app.route('/', methods=['GET'])
def hello_world():
    """
        This method is used to return hello mec developer response
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    return Response("Hello MEC Developer")


@app.route('/v1/monitor/persons', methods=['POST'])
def upload():
    """
    图像录入
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    person_info = request.values
    if 'file' not in request.files:
        raise IOError('No file')

    files = request.files.getlist("file")
    for file in files:
        if allowed_file(file.filename):
            if person_info is not None and "person_name" in person_info:
                file.filename = person_info["person_name"]
                if ".jpg" not in file.filename:
                    file.filename = file.filename + ".jpg"
            file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
        else:
            raise IOError('picture format is error')

    upload_files = []
    for file in files:
        upload_files.append(('file',
                             open(os.path.join(app.config['UPLOAD_PATH'], file.filename), 'rb')))
    rest_client = CLIENT_FACTORY.get_client_by_service_name(constants.FACE_RECOGNITION_SERVICE)
    url = rest_client.get_endpoint() + "/v1/face-recognition/upload"
    response = rest_client.post(url, None, upload_files)
    return response.text


@app.route('/v1/monitor/<person_name>')
def monitor_person(person_name):
    """
        This method is used to retrieve person information
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.PERSON_MAXSIZE)

    if path.exists(app.config['UPLOAD_PATH'] + person_name):
        return send_from_directory(app.config['UPLOAD_PATH'], person_name)

    return Response("Image " + person_name + " doesn't exist")


@app.route('/v1/monitor/persons')
def monitor_persons():
    """
        This method is used to retrieve all person information
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    url = constants.FRONTEND_URL + "/uploadFile"
    upload_files = []
    for _, _, files in os.walk(app.config['UPLOAD_PATH']):
        for file in files:
            upload_files.append(('file',
                                 open(os.path.join(app.config['UPLOAD_PATH'], file), 'rb')))
    requests.post(url, files=upload_files)
    return Response("upload success")


@app.route('/v1/monitor/persons/<person_name>', methods=['DELETE'])
def delete_person(person_name):
    """
    This method is used to delete person information
    param: person_name
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.PERSON_MAXSIZE)

    person = person_name
    person_name = person_name[0:-4]
    rest_client = CLIENT_FACTORY.get_client_by_service_name(constants.FACE_RECOGNITION_SERVICE)
    url = rest_client.get_endpoint() + "/v1/face-recognition/{0}".format(person_name)
    response = rest_client.delete(url)
    if response:
        os.remove(app.config['UPLOAD_PATH'] + person)
        time.sleep(1)
        for msg in reversed(range(len(listOfMsgs))):
            if listOfMsgs[msg]['relatedObj'] == person_name:
                del listOfMsgs[msg]
        return jsonify({'Result': 'delete success'})

    return jsonify({"Result": "the name is not exist"})


@app.route('/v1/monitor/messages')
def monitor_messages():
    """
        This method is used to return list of messages
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    list_of_msgs = []
    for msg in listOfMsgs:
        person_info = msg.copy()
        current_time = time.time()
        person_info["highlight"] = "False"
        if current_time - person_info["time"] < 15:
            person_info["highlight"] = "True"
        if current_time - person_info["time"] < 15 and person_info["cam_flag"] == "enable":
            person_info["highlight"] = "True"
        person_info["time"] =\
            datetime.datetime.fromtimestamp(person_info["time"]).strftime("%Y%m%d-%H:%M:%S")
        list_of_msgs.append(person_info)
    return jsonify(list_of_msgs)


@app.route('/v1/monitor/persons/<person_name>/messages')
def query_person(person_name):
    """
        This method is used to return specific person information
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    if len(person_name) >= 64:
        raise ValidationError(constants.PERSON_MAXSIZE)

    for msg in listOfMsgs:
        if msg["relatedObj"] == person_name:
            return jsonify(msg)
    return Response("person name " + person_name + " doesn't exist")


def start_server(handler):
    """
        This method is used to start the monitoring application server
    """
    logging.basicConfig(level=logging.INFO)
    app.logger.addHandler(handler)
    global CLIENT_FACTORY
    CLIENT_FACTORY = clientsdk.ClientFactory(listOfServices)
    if config.SSL_ENABLED:
        context = (config.SSL_CERTFILEPATH, config.SSL_KEYFILEPATH)
        app.run(host=config.SERVER_ADDRESS, debug=True,
                ssl_context=context, threaded=True, port=config.SERVER_PORT)
    else:
        app.run(host=config.SERVER_ADDRESS, debug=True, threaded=True, port=config.SERVER_PORT)
