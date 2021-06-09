人脸识别服务
===
此 repo 用于基于 osdt mep 开发应用程序
-----
这是一个人脸识别微服务的应用程序。该服务被开发
基于github上一个开放的人脸识别项目。该项目的特点是
通过以下：

使用世界上最简单的人脸识别库从 Python 或命令行识别和操作人脸。

使用 dlib 通过深度学习构建的最先进的人脸识别技术构建。该模型的准确率为 99.38%
Wild 基准测试中的 Labeled Faces。

这还提供了一个简单的 face_recognition 命令行工具，可让您对图像文件夹进行人脸识别
从命令行！

人脸识别微服务具有以下功能：人脸上传、人脸比对、人脸识别、视频人脸识别。

使用redis和postgresql存储数据

特征
===
人脸上传
------
将只有一张人脸的图片文件导入redis数据库并存入postgresql<br>
RESTful API ：POST http://127.0.0.1:9999/v1/face-recognition/upload<br>
支持多个图片文件同时上传<br>
输入：<br>
curl --request POST \
  --url http://127.0.0.1:9999/v1/face_recognition/upload \
  --header '缓存控制：无缓存' \
  --header '内容类型：多部分/表单数据；边界=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form 文件=@picture.jpg<br>
  
脸比较
-------
导入两张带有人脸的图片进行比较 <br>
RESTful API ：POST http://127.0.0.1:9999/v1/face-recognition/comparsion<br>
支持多张人脸对比<br>
输入：<br>
curl --request POST \
  --url http://127.0.0.1:9999/v1/face-recognition/comparsion \
  --header '缓存控制：无缓存' \
  --header '内容类型：多部分/表单数据；边界=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form file1=@picture1.jpg \
  --form file2=@picture2.jpg<br>

人脸识别
------
输入未知名称的图片文件，匹配redis数据库中对应的人名<br>
RESTful API ：POST http://127.0.0.1:9999/v1/face-recognition/recognition<br>
输入图像中可以有多个人脸<br>
输入：<br>
curl --request POST \
  --url http://127.0.0.1:9999/v1/face-recognition/recognition \
  --header '缓存控制：无缓存' \
  --header '内容类型：多部分/表单数据；边界=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form 文件=@picture.jpg<br>

人脸合集
--------
从摄像头获取人脸图像，url为摄像头IP<br>
RESTful API ：POST http://127.0.0.1:9999/v1/face-recognition/collection<br>
正文：{"url":"192.168.15.120"}<br>

视频人脸识别
--------
从摄像头获取人脸视频，在数据库中找到人脸名称。url为摄像头IP<br>
RESTful API ：POST http://127.0.0.1:9999/v1/face-recognition/video<br>
正文：{"url":"192.168.15.120"}<br>

刷新redis
------
将mysql中的人脸图片刷新到redis数据库
restfull API：POST http://127.0.1:9999/v1/face-recognition/refresh<br>
输入：<br>
curl --request POST \
  --url http://127.0.0.1:9999/v1/face-recognition/refresh \
  --header '缓存控制：无缓存' \

安装
===
要求
-----
Python 3.6 redis dlib face_recognition<br>
docker docker-compose<br>
macOS 或 Linux（Windows 未得到官方支持，但可能有效）<br>
安装选项：(ubuntu18.04)<br>
第三方库：cmake dlib face_recognition flask redis opencv-python requests psycopg2-binary

建造
-----
构建 docker 镜像：docker build 。 -t face_recognition:v1.4<br>
泊坞窗标签 face_recognition:v1.4 159.138.11.6:8089/face_recognition:v1.4<br>
码头推 159.138.11.6:8089/人脸识别:v1.4<br>
# 发布docker镜像到dockergub<br>
测试：python3 test.py

部署
------
1.包装图
helm install 人脸识别
2.部署
kubectl apply -f face_recognition_v1.0.yaml

Python模块
----
您可以导入 face_recognition 模块，然后只需几行代码即可轻松操作人脸。<br>
API 文档：https://face-recognition.readthedocs.io。