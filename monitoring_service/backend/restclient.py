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
import constants
import config


def get_access_token():
    url = constants.mep_agent_url + "/mep-agent/v1/token"
    headers = {'Content-Type': constants.contentType}
    if config.ssl_enabled:
        url = constants.httpsUrl + url
        response = requests.get(url, headers=headers, verify=config.ssl_cacertpath)
    else:
        url = constants.httpUrl + url
        response = requests.get(url, headers=headers)
    # extracting data in json format
    data = response.json()
    access_token = data["access_token"]
    return access_token


class RestClient:
    # rest client constructor
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def post(self, url, body=None, **kwargs):
        if constants.access_token_enabled and constants.ssl_enabled:
            access_token = get_access_token()
            headers = {'Content-Type': constants.contentType, 'Authorization': access_token}
            response = requests.post(url, data=body, headers=headers, verify=config.ssl_cacertpath, **kwargs)
        else:
            response = requests.post(url, data=body, **kwargs)
        return response

    def delete(self, url, **kwargs):
        if constants.access_token_enabled and constants.ssl_enabled:
            access_token = get_access_token()
            headers = {'Content-Type': constants.contentType, 'Authorization': access_token}
            response = requests.delete(url, headers=headers, verify=config.ssl_cacertpath, **kwargs)
        else:
            response = requests.delete(url, **kwargs)
        return response

    def get_endpoint(self):
        return self.endpoint
