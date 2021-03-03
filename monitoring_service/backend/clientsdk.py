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
Implementation of client factory
"""
import requests
import restclient

clientObjects = {}


def get_service_endpoint(service):
    """
       This is a get service endpoint method for getting endpoint information by using service name
    """
    url = restclient.MEP_AGENT_URL + "/mep-agent/v1/endpoint/{0}".format(service)
    headers = {'Content-Type': "application/json"}
    if restclient.SSL_ENABLED:
        url = restclient.HTTPS_URL + url
        response = requests.get(url, headers=headers, verify=restclient.SSL_CACERTPATH)
    else:
        url = restclient.HTTP_URL + url
        response = requests.get(url, headers=headers)

    # extracting data in json format
    if response:
        data = response.json()
        url = data["uris"]
        return url[0]
    return ""


class ClientFactory:
    """
       This is a class for client factory implementation.
    """
    #  constructor
    def __init__(self, list_of_services):
        self.update_client_object(list_of_services)

    def update_client_object(self, list_of_services):
        """
           This is a update client object method to get endpoint information
        """
        for service in list_of_services:
            endpoint = get_service_endpoint(service)
            if endpoint != "" and "http" in endpoint or "https" in endpoint:
                clientObjects[service] = restclient.RestClient(endpoint)

    def get_client_by_service_name(self, service):
        """
           This is a get client by service name method to return client object by using service name
        """
        return clientObjects[service]

