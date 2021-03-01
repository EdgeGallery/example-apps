﻿# example-apps

#### 介绍
Example applications based on EdgeGallery

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)

### How to develop an example application

1.Consumer application can easily integrate with MEP/MEP-AGENT to obtain producer application services

2.Every consumer application should be writing 2 to 3 lines of code to acheive this functionality

3.Mep-agent should expose an API’s to get token and service endpoint

4.Consumer application uses consumer client to perform CRUD operations.

5.Example consumer application can leverage mep-agent and consumerclient to communicate with mep-service via kong

6. ClientFactory code is implemented to send request to mep-agent to get service endpoint and based on endpoint information will create a client object
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

7.Consumerclient code is implemented to get access token and send request to mep service via kong
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
        access_token = "Bearer " + access_token
        headers = {'Authorization': access_token}
        response = requests.post(url, data=body, files=upload_files, headers=headers, verify=False)
        return response
    def delete(self, url):
        access_token = get_access_token()
        access_token = "Bearer " + access_token
        headers = {'Authorization': access_token}
        response = requests.delete(url, headers=headers, verify=False)
        return response
    def get_endpoint(self):
        return self.endpoint

8.Application code is implemented to send request to consumer client for communicating with mep service via kong api gateway
rest_client = clientFactory.get_client_by_service_name(constants.face_recognition_service)
url = rest_client.get_endpoint() + "/v1/face-recognition/recognition"
response = rest_client.post(url, body)



