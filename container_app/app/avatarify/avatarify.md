Avatarify
---------------
This is an application to get photorealistic avatars for any video stream or video files. <br>
This application is developed based on open source project [avatarify-python](https://github.com/alievk/avatarify-python)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. Provided APIs could be used by producer applications for use cases like video conferencing, AR/VR gaming<br>

Usage Steps:
--------------
<h4> Avatarify for video files</h4>
Step 1: Add your customized avatar(URI: /avatarify/add-avatar) <br>
Step 2: Upload the video file (URI: /avatarify/upload-video) and get the outputId from the response<br>
Step 3: Get the avatarify with given outputId (URI: avatarify/start?id={outputId}), open the url received in the<br>response in s browser.

<h4> Avatarify for video stream</h4>
Step 1: Add your customized avatar(URI: /avatarify/add-avatar) <br>
Step 2: Add the video stream by adding camera (URI: /avatarify/add-camera) and get the outputId from the response<br>
Step 3: Get the avatarify with given outputId (URI: avatarify/start?id={outputId}), open the url received in the<br>response in s browser.

Avatarify Interface 
----------------
<h4>1. Input image avatar</h4>
Input the image file and upload the your custome avatar <br>

Resource URI: /avatarify/add-avatar<br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| image     | file                     | your avatar image|

Example Request:

```
curl --location --request POST 'http://127.0.0.1:31650/avatarify/add-avatar' \
--form 'image=@"cute.jpeg"'
```
Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| status     | string                     | Upload success message |

Return Code: 200 OK

Example Response:
```
{
    "message": "Avatar successfully uploaded"
}
```

<h4>2. Input video file</h4>
Input the video file and get the outputId as response <br>

Resource URI: /avatarify/upload-video<br>
Method: POST<br>

Body parameters:
| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| file     | file                     | your input video|


Example Request:

```
curl --location --request POST 'http://127.0.0.1:31650/avatarify/upload-video' \
--form 'file=@"testvideo.mp4"'
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| message     | string                     | avtarify video upload success message|
| outputId     | string                     | outputId for starting avatarify|

Return Code: 200 OK

Example Response:
```
{
    "message": "File successfully uploaded",
    "outputId": "4ff4a378776607b6daff536d9115063a"
}
```

<h4>3. Input video stream and camera name</h4>
Input the video stream, camere name and get the outputId as response <br>

Resource URI: /avatarify/add-camera<br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| name     | text                     | camera name|
| url     | text                     | URL of input stream, Eg: rtps://x.x.x.x/stream|


Example Request:

```
curl --location --request POST 'http://127.0.0.1:31650/avatarify/add-camera' \
--form 'name="cam1"' \
--form 'url="rtsp://192.168.1.8/testvideonew.mkv"'
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| message     | string                     | avtarify add camera success message|
| outputId     | string                     | outputId for starting avatarify|

Return Code: 200 OK

Example Response:
```
{
    "message": "Camera added successfully",
    "outputId": "81b8dd33dd5c093a73093f0c990c59e3"
}
```

<h4>4. Get the avatarify output</h4>
Input outputId and get the avatarify output URL and execute in browser <br>

Resource URI: /avatarify/start<br>
Method: GET<br>

Request parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| id     | string                     | outputId of upload video or add camera|


Example Request:

```
curl --location --request GET 'http://{{MEP_IP}}:31650/avatarify/start?id=016ad770730981ca72c5d8ea06bf2e90'
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| status     | string                     | Status with avtarify URL for link                |

Return Code: 200 OK

Example Response:
```
HTTP/1.1 200 OK
"Started avatarify on http://{MEP_IP}:31650/camid/329833d58f77c618d90cee4d905664d5"
```

<h4>5. Stop the avatarify streaming</h4>
Stop the avatarify streaming. <br>

Resource URI: /avatarify/stop<br>
Method: POST<br>

Example Request:

```
curl --location --request POST 'http://127.0.0.1:31650/avatarify/stop'
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| status     | string                     | avtarify stopped status                 |

Return Code: 200 OK

Example Response:
```
HTTP/1.1 200 OK
"Stopped avatarify"
```

<h4>6. Delete your avatar which is added </h4>
Delete the avatar which is added. <br>

Resource URI: /avatarify/delete-avatar<br>
Method: DELETE<br>

Example Request:

```
curl --location --request DELETE 'http://127.0.0.1:31650/avatarify/delete-avatar'
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| status     | string                     | avtarify delete message|

Return Code: 200 OK

Example Response:
```
{
    "message": "Avatar successfully deleted"
}
```
<h4>7. Play avatarify uploaded video</h4>
Input outputId and play the video in browser <br>

Resource URI: /avatarify/play-video/{outputId}<br>
Method: GET<br>

Request parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| outputId     | string                     | outputId of upload video   |


Example Request:

```
curl --location --request GET 'http://127.0.0.1:31650/avatarify/play-video/016ad770730981ca72c5d8ea06bf2e90'
```

Return Code: 200 OK

Example Response:
Play video in browser

Exception status code

| HTTP Status Code | Description |
| --- | --- |
| 400  | Bad request, used to indicate that connection wrong. |