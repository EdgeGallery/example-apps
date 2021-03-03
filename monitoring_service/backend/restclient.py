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
Implementation of rest client
"""
import os
import requests

HTTP_URL = "http://"
HTTPS_URL = "https://"
MEP_AGENT_URL = os.environ.get("MEP_AGENT", "edgegallery.org")
SSL_ENABLED = False
ACCESS_TOKEN_ENABLED = False
CONTENT_TYPE = "application/json"
SSL_CACERTPATH = "/usr/app/ssl/ca.crt"


def get_access_token():
    """Get access token from mep-agent and return access token."""
    url = MEP_AGENT_URL + "/mep-agent/v1/token"
    headers = {'Content-Type': CONTENT_TYPE}
    if SSL_ENABLED:
        url = HTTPS_URL + url
        response = requests.get(url, headers=headers, verify=SSL_CACERTPATH)
    else:
        url = HTTP_URL + url
        response = requests.get(url, headers=headers)
    # extracting data in json format
    data = response.json()
    access_token = data["access_token"]
    return access_token


class RestClient:
    """
       This is a class for rest client implementation.
    """
    # rest client constructor
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def post(self, url, body=None, upload_files=None):
        """
           This is a post method for calling mep service via kong
        """
        access_token = get_access_token()
        access_token = "Bearer " + access_token
        headers = {'Authorization': access_token}
        response = requests.post(url, data=body, files=upload_files,
                                 headers=headers, verify=False)
        return response

    def delete(self, url):
        """
           This is a delete method for calling mep service via kong
        """
        access_token = get_access_token()
        access_token = "Bearer " + access_token
        headers = {'Authorization': access_token}
        response = requests.delete(url, headers=headers, verify=False)
        return response

    def get_endpoint(self):
        """
           This is a get endpoint method for getting endpoint information
        """
        return self.endpoint
		
