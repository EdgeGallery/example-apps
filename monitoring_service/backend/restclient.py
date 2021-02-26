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

import requests
import os

httpUrl = "http://"
httpsUrl = "https://"
mep_agent_url = os.environ.get("MEP_AGENT", "edgegallery.org")
ssl_enabled = False
access_token_enabled = False
contentType = "application/json"
ssl_cacertpath = "/usr/app/ssl/ca.crt"


def get_access_token():
    url = mep_agent_url + "/mep-agent/v1/token"
    headers = {'Content-Type': contentType}
    if ssl_enabled:
        url = httpsUrl + url
        response = requests.get(url, headers=headers, verify=ssl_cacertpath)
    else:
        url = httpUrl + url
        response = requests.get(url, headers=headers)
    # extracting data in json format
    data = response.json()
    access_token = data["access_token"]
    return access_token


class RestClient:
    # rest client constructor
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def post(self, url, body=None, upload_files=None):
        access_token = get_access_token()
        access_token = access_token
        headers = {'Authorization': access_token}
        response = requests.post(url, data=body, files=upload_files, headers=headers, verify=False)
        return response

    def delete(self, url):
        access_token = get_access_token()
        access_token = access_token
        headers = {'Authorization': access_token}
        response = requests.delete(url, headers=headers, verify=False)
        return response

    def get_endpoint(self):
        return self.endpoint
