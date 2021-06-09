# 示例应用

#### 介绍
基于 EdgeGallery 的示例应用程序

### 如何开发示例应用程序

1.消费者应用可以方便地与MEP/MEP-AGENT集成，获得生产者应用服务

2.每个消费者应用程序都应该编写 2 到 3 行代码来实现此功能

3.Mep-agent 应该公开一个 API 来获取令牌和服务端点

4.Consumer 应用程序使用消费者客户端来执行 CRUD 操作。

5.示例消费者应用程序可以利用 mep-agent 和 consumerclient 通过 kong 与 mep-service 通信

6.ClientFactory 代码实现向 mep-agent 发送请求以获取服务端点，并根据端点信息创建一个客户端对象

def get_service_endpoint(service):

    url = restclient.mep_agent_url + "/mep-agent/v1/endpoint/{0}".format(service)
    headers = {'Content-Type': "application/json"}
    如果 restclient.ssl_enabled：
        url = restclient.httpsUrl + url
        response = requests.get(url, headers=headers, verify=restclient.ssl_cacertpath)
    别的：
        url = restclient.httpUrl + url
        response = requests.get(url, headers=headers)
    # 以json格式提取数据
    如果回应：
        数据 = response.json()
        url = 数据["uris"]
        返回网址[0]
    别的：
        返回 ””

类客户端工厂：

    # 构造函数
    def __init__(self, list_of_services):
        self.update_client_object(list_of_services)
    def update_client_object(self, list_of_services):
        对于 list_of_services 中的服务：
            端点 = get_service_endpoint(service)
            如果端点 != "" 和 "http" 在端点或 "https" 在端点：
                    clientObjects[service] = restclient.RestClient(endpoint)
    def get_client_by_service_name(self, service):
        返回客户端对象[服务]

7.Consumerclient代码实现获取访问令牌并通过kong向mep服务发送请求

def get_access_token():

    url = mep_agent_url + "/mep-agent/v1/token"
    headers = {'Content-Type': contentType}
    如果 ssl_enabled：
        url = httpsUrl + url
        response = requests.get(url, headers=headers, verify=ssl_cacertpath)
    别的：
        url = httpUrl + url
        response = requests.get(url, headers=headers)
    # 以json格式提取数据
    数据 = response.json()
    access_token = 数据["access_token"]
    返回 access_token
类 RestClient：

    # 休息客户端构造函数
    def __init__(self,endpoint):
        self.endpoint = 端点
    def post(self, url, body=None,upload_files=None):
        access_token = get_access_token()
        access_token = "Bearer " + access_token
        headers = {'授权'：access_token}
        response = requests.post(url, data=body, files=upload_files, headers=headers, verify=False)
        返回响应
    定义删除（自我，网址）：
        access_token = get_access_token()
        access_token = "Bearer " + access_token
        headers = {'授权'：access_token}
        response = requests.delete(url, headers=headers, verify=False)
        返回响应
    def get_endpoint(self):
        返回 self.endpoint

8.应用代码实现向消费者客户端发送请求，通过kong api网关与mep服务进行通信

    rest_client = clientFactory.get_client_by_service_name(constants.face_recognition_service)
    url = rest_client.get_endpoint() + "/v1/face-recognition/recognition"
    response = rest_client.post(url, body)