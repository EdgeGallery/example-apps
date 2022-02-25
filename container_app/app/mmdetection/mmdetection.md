MMDetection
---------------
MMDetection is an open source object detection toolbox based on PyTorch. It is a part of the OpenMMLab project.<br>
This application is developed based on open source project [MMDetection](https://github.com/open-mmlab/mmdetection) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Option 1: Provide input video to detect objects and generates video with detected objects being marked (URI: /mmdetection/v1/detect_video) <br>
Option 2: Provide input image to detect objects and generates image with detected objects being marked (URI: /mmdetection/v1/detect_image) <br>

MMDetection Interface 
----------------
<h4>1. Detects objects in a video </h4>
Input (video file) and obtain video file detected objects. <br>

Resource URI: /mmdetection/v1/detect_video <br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | video mp4 file   | Yes |

Return Parameters:

    Video file

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/mmdetection/v1/detect_video' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@demo.mp4;type=video/mp4'
```

<h4>2. Detects objects in a image </h4>
Input (image file) and obtain image file detected objects. <br>

Resource URI: /mmdetection/v1/detect_image <br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | video mp4 file   | Yes |

Return Parameters:

    Image file

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/mmdetection/v1/detect_image' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@demo.jpg;type=image/jpeg'
```