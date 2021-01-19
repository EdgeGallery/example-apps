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

import config

# [Constants]
httpUrl = "http://"
httpsUrl = "https://"
recognition_url = config.api_gateway
mep_agent_url = config.mep_agent
frontend_url = httpUrl + config.fe_service
face_position = "Face position"
received_message = "Received message from ClientIP ["
operation = "] Operation ["
resource = " Resource ["
person_maxsize = "length of the person name is larger than max size"
contentType = "application/json"
frontOfCamera = " has appeared in front of camera "
face_recognition_service = "facerecognition_service"
WAIT_SECONDS = 1
PERSON_TIMEOUT_SECONDS = 15
access_token_enabled = False
ssl_enabled = False