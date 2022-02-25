body_pose_picture
==============
This is an application to infer human body poses <br>
This application is developed based on ascend project [body_pose_picture](https://gitee.com/ascend/samples/tree/master/python/contrib/body_pose_picture)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (jpg or mp4 file) to infer human body poses and obtain output image or video (URI: /ascend/v1/body_pose_picture/input) <br>


body_pose_picture Interface 
----------------
<h4>1. Input image or video file</h4>
Input image or video file and obtain result image or video <br>

Resource URI: /ascend/v1/body_pose_picture/input<br>
Method: POST<br>

Request parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file | file                      | jpg or mp4 file     | Yes |

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| file     | file                     | output file in jpg or mp4 format        |

Example Request:

```
curl -X 'POST' \
  'http://{{HOST_IP}}:{{PORT}}/ascend/v1/body_pose_picture/input' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test.jpg'
```
Example Response:

```
HTTP/1.1 200 OK
<<File output>>
```