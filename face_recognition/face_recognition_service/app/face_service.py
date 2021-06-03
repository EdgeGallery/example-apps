#!/usr/bin/python
# -*- coding: utf-8 -*-
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
This is an app application for face recognition services.
the feature vector of the face.
Store face images in data volume postgres
Author e-mail:zhanghailong22@huawei.com
"""
import time
import io
import cv2
import numpy as np
import redis
from flask import make_response, jsonify
import requests
import psycopg2
import face_recognition
import app.config


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
POSTGRES_HOST = app.config.postgres_host
POSTGRES_USER = app.config.postgres_user
POSTGRES_DATABASE = app.config.postgres_database
POSTGRES_PASSWORD = app.config.postgres_password
REDIS_HOST = app.config.redis_host


def allowed_file(filename):
    """
    允许上传的文件类型：png、jpg、jpeg
    param: filename:
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def camera(url):
    """
    拍照采集人脸
    param: url 摄像机地址
    """
    video_capture = cv2.VideoCapture(url)
    while True:
        _, frame = video_capture.read()
        frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)
        # Resize frame of video to 1/4 size for faster face recognition processing
        # Only process every other frame of video to save time
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def take_photo(url):
    """
    拍照采集人脸
    param: url 摄像机地址
    """
    start = time.clock()
    video_capture = cv2.VideoCapture(url)
    while True:
        _, frame = video_capture.read()
        frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # usegeneratorFunction output video stream，Output per requestcontentType isimages/jpeg
        if frame is None:
            return make_response(jsonify({'result': 'camera url is error'}), 403)
        ret, jpeg = cv2.imencode('.jpg', small_frame)
        end = time.clock()
        if (end - start) > 1:
            video_capture.release()
            return jpeg


def face_upload(img, file_image):
    """
    人脸信息上传
    param: img, file
    """
    # connectionredis
    try:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
        redis_connection = redis.Redis(connection_pool=pool)
    except redis.ConnectionError:
        print('redis connection is error')
    image = face_recognition.load_image_file(file_image)
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) != 1:
        raise IOError('face number is only one')
    if file_image and allowed_file(file_image.filename):
        # Save aspostgresIn the database
        try:
            conn = psycopg2.connect(host=POSTGRES_HOST, user=POSTGRES_USER,
                                    password=POSTGRES_PASSWORD, database=POSTGRES_DATABASE,
                                    port=5432)
            cur = conn.cursor()
        except requests.RequestException:
            print('postgres connection is error')
        cur.execute("select exists(select * from information_schema.tables where table_name=%s)",
                    ('image_data',))
        if cur.fetchone()[0] == 0:
            # create table cataract
            command = "create table if not exists image_data " \
                      "(name text PRIMARY KEY NOT NULL, image bytea NOT NULL);"
            cur.execute(command)
            r_command = "create rule  r_image_data as on insert to image_data where exists " \
                        "(select 1 from image_data where name =new.name) do instead nothing;"
            cur.execute(r_command)
            conn.commit()  # commit the changes
        name = file_image.filename[0:-4]
        # create table cataract
        command = "insert into image_data(name, image) values(%s, %s);"
        params = (name, psycopg2.Binary(img))
        cur.execute(command, params)
        conn.commit()
        cur.close()
        conn.close()
    else:
        raise IOError('picture format is error')
    face_encodings = face_recognition.face_encodings(image, face_locations)
    # evenredisdatabase
    # Enter the person's name-Corresponding feature vector
    redis_connection.set(name, face_encodings[0].tobytes())


def face_find(file_image):
    """
    人脸信息查找
    param: file
    """
    # connectionredis
    try:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
        redis_connection = redis.Redis(connection_pool=pool)
    except redis.ConnectionError:
        print('redis connection is error')

    image = face_recognition.load_image_file(file_image)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    # Take out all the names of people and their corresponding feature vectors
    names = redis_connection.keys()
    faces = redis_connection.mget(names)
    # Make up a matrix，Calculate similarity（Euclidean distance）
    find_names = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([np.frombuffer(x) for x in faces], face_encoding, tolerance=0.42)
        num = 0
        for name, match in zip(names, matches):
            num = num + 1
            if match:
                face_name = {'Name': str(name, 'utf-8'),
                             'Face position': {'top': top, 'right': right,
                                               'bottom': bottom, 'left': left}}
                find_names.append(face_name)
                break
            if matches[-1] == 0 and len(matches) == num:
                face_name = {'Name': 'unknown',
                             'Face position': {'top': top, 'right': right,
                                               'bottom': bottom, 'left': left}}
                find_names.append(face_name)
    return find_names


def face_compare(file1, file2):
    """
    人脸信息对比
    param: file1, file2
    """
    image1 = face_recognition.load_image_file(file1)
    face_locations1 = face_recognition.face_locations(image1)
    face_encodings1 = face_recognition.face_encodings(image1)
    image2 = face_recognition.load_image_file(file2)
    face_locations2 = face_recognition.face_locations(image2)
    if len(face_locations2) != 1:
        raise IOError('face number is only one')
    face_encodings2 = face_recognition.face_encodings(image2)[0]
    face_distances = face_recognition.face_distance(face_encodings1, face_encodings2)
    result = []
    for (top, right, bottom, left), distance in zip(face_locations1, face_distances):
        face_local = {'Similarity': 1 - distance,
                      'Face position': {'top': top, 'right': right,
                                        'bottom': bottom, 'left': left}}
        result.append(face_local)
    return result


def refresh_redis():
    """
    刷新redis
    """
    # connectionredis
    try:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
        redis_connection = redis.Redis(connection_pool=pool)
    except redis.ConnectionError:
        print('redis connection is error')
    # 1.connectionmysqldatabase
    try:
        conn = psycopg2.connect(host=POSTGRES_HOST, user=POSTGRES_USER,
                                password=POSTGRES_PASSWORD, database=POSTGRES_DATABASE,
                                port=5432)
    except requests.RequestException:
        print('postgres connection is error')
    # 2.Create cursor
    cursor = conn.cursor()
    sql = "select * from image_data"
    cursor.execute(sql)  # 执行sql
    # Query all data，The returned result is in the form of a tuple by default，So iterative processing
    for i in cursor.fetchall():
        name = i[0]  # get name
        data = i[1]  # get data
        # file = Image.open(BytesIO(data))
        image = face_recognition.load_image_file(io.BytesIO(data))
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        # Enter the person's name-Corresponding feature vector
        redis_connection.set(name, face_encodings[0].tobytes())
    cursor.close()
    conn.close()
    number = redis_connection.keys()
    return number


def video_camera(file_image):
    """
    视频监控/笔记本
    param: file
    """
    # connectionredis
    pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
    redis_connection = redis.Redis(connection_pool=pool)
    # Connect to the database
    # Take out all the names of people and their corresponding feature vectors
    names = redis_connection.keys()
    known_faces = redis_connection.mget(names)
    if file_image == "0":
        file_image = int(file_image)
    video_capture = cv2.VideoCapture(file_image)
    # Initialize some variables
    face_locations = []
    face_names = []
    process_this_frame = 0
    while True:
        # Grab a single frame of video
        _, frame = video_capture.read()
        if frame is None:
            return make_response(jsonify({'result': 'camera url is error'}), 403)
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # Convert the image from BGR color  to RGB color
        rgb_small_frame = small_frame[:, :, ::-1]
        # Only process every other frame of video to save time
        if process_this_frame == 0:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces([np.frombuffer(x) for x in known_faces],
                                                         face_encoding, tolerance=0.52)
                name = "Unknown"
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    [np.frombuffer(x) for x in known_faces], face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = str(names[best_match_index], 'utf-8')
                face_names.append(name)
        process_this_frame = process_this_frame + 1
        if process_this_frame == 20:
            process_this_frame = 0
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


def web_video(url):
    """
    视频监控/摄像头
    param: file
    """
    # connectionredis
    try:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
        redis_connection = redis.Redis(connection_pool=pool)
    except redis.ConnectionError:
        print('redis connection is error')
    # Connect to the database
    # Take out all the names of people and their corresponding feature vectors
    names = redis_connection.keys()
    known_faces = redis_connection.mget(names)
    face_locations = []
    face_names = []
    process_this_frame = 0
    if url == "0" or url == '1':
        url = int(url)
    video_capture = cv2.VideoCapture(url)
    while True:
        _, frame = video_capture.read()
        frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # Convert the image from BGR color  to RGB color
        rgb_small_frame = small_frame[:, :, ::-1]
        # Only process every other frame of video to save time
        if process_this_frame == 0:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces([np.frombuffer(x) for x in known_faces],
                                                         face_encoding, tolerance=0.42)
                name = "Unknown"
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    [np.frombuffer(x) for x in known_faces], face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = str(names[best_match_index], 'utf-8')
                face_names.append(name)
        process_this_frame = process_this_frame + 1
        if process_this_frame == 50:
            process_this_frame = 0
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def face_delete(name):
    """
    人脸信息删除
    param: name
    """
    # connectionredis
    try:
        pool = redis.ConnectionPool(host=REDIS_HOST, port=6379)
        redis_connection = redis.Redis(connection_pool=pool)
    except redis.ConnectionError:
        print('redis connection is error')
    # Query in the database
    try:
        conn = psycopg2.connect(host=POSTGRES_HOST, user=POSTGRES_USER,
                                password=POSTGRES_PASSWORD, database=POSTGRES_DATABASE,
                                port=5432)
        cur = conn.cursor()
    except requests.RequestException:
        print('postgres connection is error')
    r_command = "delete FROM image_data WHERE name='%s'" % name
    cur.execute(r_command)
    conn.commit()  # commit the changes
    conn.close()
    result = redis_connection.delete(name)
    return result


