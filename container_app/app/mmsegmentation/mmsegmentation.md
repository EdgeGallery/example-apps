MMSegmentation
---------------
MMSegmentation is an open source semantic segmentation toolbox based on PyTorch. It is a part of the OpenMMLab project.<br>
This application is developed based on open source project [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Option 1: Provide input video to detect objects and generates video with segmented objects (URI: /mmsegmentation/v1/detect_video) <br>
Option 2: Provide input image to detect objects and generates image with segmented objects (URI: /mmsegmentation/v1/detect_image) <br>

MMSegmentation Interface 
----------------
<h4>1. Segments objects in a video </h4>
Note: For segmentation in video file it's recommended to use GPU and change detectvideo.sh. <br><br>

Input (video file) and obtain video file with segmented objects. <br>

Resource URI: /mmsegmentation/v1/detect_video <br>
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
  'http://127.0.0.1:8000/mmsegmentation/v1/detect_video' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@demo.mp4;type=video/mp4'
```

<h4>2. Segments objects in a image </h4>
Input (image file) and obtain image file with segmented objects. <br>

Resource URI: /mmsegmentation/v1/detect_image <br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | image file   | Yes |

Return Parameters:

    Image file

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/mmsegmentation/v1/detect_image' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@demo.png;type=image/png'
```