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

from flask import Flask, Response
import config
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/v1/monitor/cameras', methods=['POST'])
def add_camera():
    camera_info = request.json
    app.logger.info("Received message from ClientIP [" + request.remote_addr + "] Operation [" + request.method + "]" +
                    " Resource [" + request.url + "]")
    camera_info = {"name": camera_info["name"], "rtspurl": camera_info["rtspurl"], "location": camera_info["location"]}
    listOfCameras.append(camera_info)
    return Response("success")


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