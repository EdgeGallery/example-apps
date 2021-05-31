#!/usr/bin/python
# -*- coding: utf-8 -*-
# test face_recognition_app.py
#
import psycopg2
import redis
import requests

# 录入
# host = "http://127.0.0.1:9999"
# url = host+"/v1/face-recognition/upload"
#
# path_upload = '../test/zhanghailong.png'
# split_path1 = path_upload.split('/')
# filename1 = split_path1[-1]
#
# path_upload_2 = '../test/zhanghailong1.png'
# split_path2 = path_upload_2.split('/')
# filename2 = split_path2[-1]
#
# file1 = open(path_upload, 'rb')
# file2 = open(path_upload_2, 'rb')
# files = [('file', (filename1, file1, 'image/jpg')), ('file', (filename2, file2, 'image/jpg'))]
# r = requests.post(url, files=files)
# result = r.text
#
# # 识别
# url = host+"/v1/face-recognition/recognition"
#
# file_path = '../test/two_people.jpg'
# split_path = file_path.split('/')
# filename3 = split_path[-1]
#
# file3 = open(file_path, 'rb')
# files = {'file': (filename3, file3, 'image/jpg')}
#
# r = requests.post(url, files=files)
# result1 = r.text
#
# # 对比
# url = host + "/v1/face-recognition/comparison"
# path_upload = '../test/two_people.jpg'
# split_path1 = path_upload.split('/')
# filename1 = split_path1[-1]
#
# path_upload_2 = '../test/obama.jpg'
# split_path2 = path_upload_2.split('/')
# filename2 = split_path2[-1]
#
# file1 = open(path_upload, 'rb')
# file2 = open(path_upload_2, 'rb')
# files = ('file1', (filename1, file1, 'image/jpg')), ('file2', (filename2, file2, 'image/jpg'))
# r = requests.post(url, files=files)
# result2 = r.text
# print(result2)
#
# # 视频监控
# url = host + "/v1/face-recognition/video"
# data = {"url": "rstp://admin:HuaWei123@192.168.15.120:554"}
# result = requests.post(url, json=data)
# result = r.text
# print(result)
#
#
# # 刷新redis
# url = "http://159.138.5.41:32116/v1/face-recognition/refresh"
#
# r = requests.post(url)
# result4 = r.text
# print(result4)

#
# url = host+"/v1/face-recognition/zhanghailong"
#
# r = requests.delete(url)
# result5 = r.text
# print(result5)

try:
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    redis_connection = redis.Redis(connection_pool=pool)
except redis.ConnectionError:
    print('redis connection is error')
redis_connection.set("name", "asdadad")