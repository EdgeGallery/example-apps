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
    Defined monitoring service constants.
"""
import config

# [Constants]
HTTP_URL = "http://"
HTTPS_URL = "https://"
RECOGNITION_URL = config.api_gateway
MEP_AGENT_URL = config.MEP_AGENT
FRONTEND_URL = HTTP_URL + config.FE_SERVICE
FACE_POSITION = "Face position"
RECEIVED_MESSAGE = "Received message from ClientIP ["
OPERATION = "] Operation ["
RESOURCE = " Resource ["
PERSON_MAXSIZE = "length of the person name is larger than max size"
CONTENT_TYPE = "application/json"
FRONT_OF_CAMERA = " has appeared in front of camera "
FACE_RECOGNITION_SERVICE = "facerecognition_service"
WAIT_SECONDS = 1
PERSON_TIMEOUT_SECONDS = 15
ACCESS_TOKEN_ENABLED = False
SSL_ENABLED = False