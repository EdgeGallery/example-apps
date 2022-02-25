Open Pose
---------------
Open pose is meant for real time human pose estimation. OpenPose has represented the first real-time multi-person system to jointly detect human body, hand, facial, and foot keypoints (in total 135 keypoints) on single images.<br>
This application is developed based on open source project [Open Pose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. Provided APIs can be used by consumer applications for usecases like:<br>
- Activity Recognition
    - Applications to detect if a person has fallen down or is sick. <br>
    - Applications that can autonomously teach proper work out regimes, sport techniques and dance activities. <br>
    - Applications that can understand full-body sign language. (Ex: Airport runway signals, traffic policemen signals, etc.). <br>
    - Applications that can enhance security and surveillance. <br>
- Motion Capture and Augmented Reality <br>
- Training Robots <br>
- Motion Tracking for Gaming Consoles <br>

Usage Steps:
--------------
Step 1: Provide image input (image or mp4 file) and generates output-ids (URI: /openpose/v1/input) <br>
Step 2: Generate the output (image or mp4 file) with the output-ids (URI: /openpose/v1/output/{outputId}) <br>

Open pose Interface 
----------------
<h4>1. Open pose input</h4>
Input image file and generates output-id <br>

Resource URI: /openpose/v1/input<br>
Method: POST<br>

Body Parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | mp4 video file or image(.png, jpg)    | Yes |

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| outputId     | string                     | Output Id to get the file later                  |

Example Request:

```
curl -X 'POST'
  'http://{{HOST_IP}}:{{PORT}}/fawkes/v1/input'
  -H 'accept: application/json'
  -H 'Content-Type: multipart/form-data'
  -F 'file=@pose-animator.png;type=image/png'
```

Example Response:

```
HTTP/1.1 200 OK
{
    "outputId": "e0d7058c8080345569679df0a172a9cd"
}
```

<h4>2. Open pose output</h4>
Generate an image with output-id <br>

Resource URI: /openpose/v1/output/{outputId}<br>
Method: GET<br>

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| file     | file                     | output file                |

Example Request:

```
curl -X 'GET'
  'http://{{HOST_IP}}:{{PORT}}/openpose/v1/output/e0d7058c8080345569679df0a172a9cd'
  -H 'accept: application/json'
```

Example Response:

```
HTTP/1.1 200 OK
<<File output>>
```