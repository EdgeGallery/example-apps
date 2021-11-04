#
# Copyright 2021 Huawei Technologies Co., Ltd.
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
Exposed an API's of location application
"""
import os
import time
from os import path
import datetime
import json
import logging
from wsgiref.util import FileWrapper
import requests
from flask import Flask, Response, request, jsonify, send_from_directory
from flask_sslify import SSLify
from flask_cors import CORS
from marshmallow import ValidationError
import config
import constants
import clientsdk

app = Flask(__name__)
CORS(app)
sslify = SSLify(app)
app.config['JSON_AS_ASCII'] = False
app.config['supports_credentials'] = True
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
listOfServices = [constants.LOCATION_SERVICE]

@app.route('/v1/location/users', methods=['GET'])
def get_location():
    """
    Get Location
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    # rest_client = CLIENT_FACTORY.get_client_by_service_name(constants.LOCATION_SERVICE)
    # url = rest_client.get_endpoint() + "/location/v1/user?address=" + request.args.get('ueId')
    # response = rest_client.get(url)

    url = "http://127.0.0.1:9912/location/v1/user?address=" + request.args.get('ueId')
    response = requests.get(url, headers={}, verify=False)
    return response.text

@app.route('/', methods=['GET'])
def hello_world():
    """
        This method is used to return hello location app response
    """
    app.logger.info(constants.RECEIVED_MESSAGE + request.remote_addr +
                    constants.OPERATION + request.method + "]" +
                    constants.RESOURCE + request.url + "]")
    return Response("Hello, Location Application!")

def start_server(handler):
    """
        This method is used to start the location application server
    """
    logging.basicConfig(level=logging.INFO)
    app.logger.addHandler(handler)
    # global CLIENT_FACTORY
    # CLIENT_FACTORY = clientsdk.ClientFactory(listOfServices)
    if config.SSL_ENABLED:
        context = (config.SSL_CERTFILEPATH, config.SSL_KEYFILEPATH)
        app.run(host=config.SERVER_ADDRESS, debug=True,
                ssl_context=context, threaded=True, port=config.SERVER_PORT)
    else:
        app.run(host=config.SERVER_ADDRESS, debug=True, threaded=True, port=config.SERVER_PORT)
