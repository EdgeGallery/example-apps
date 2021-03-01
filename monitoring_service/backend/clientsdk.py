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
import restclient

clientObjects = {}


def get_service_endpoint(service):
    url = restclient.mep_agent_url + "/mep-agent/v1/endpoint/{0}".format(service)
    headers = {'Content-Type': "application/json"}
    if restclient.ssl_enabled:
        url = restclient.httpsUrl + url
        response = requests.get(url, headers=headers, verify=restclient.ssl_cacertpath)
    else:
        url = restclient.httpUrl + url
        response = requests.get(url, headers=headers)

    # extracting data in json format
    if response:
        data = response.json()
        url = data["uris"]
        return url[0]
    else:
        return ""


class ClientFactory:
    #  constructor
    def __init__(self, list_of_services):
        self.update_client_object(list_of_services)

    def update_client_object(self, list_of_services):
        for service in list_of_services:
            endpoint = get_service_endpoint(service)
            if endpoint != "" and "http" in endpoint or "https" in endpoint:
                    clientObjects[service] = restclient.RestClient(endpoint)

    def get_client_by_service_name(self, service):
        return clientObjects[service]
