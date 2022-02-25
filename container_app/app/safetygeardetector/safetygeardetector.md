Safety Gear Detector
---------------
This reference implementation is capable of detecting people passing in front of a camera and detecting if the people are wearing safety-jackets and hard-hats. The application counts the number of people who are violating the safety gear standards and the total number of people detected.<br>
This application is developed based on open source project [Safety Gear Detector](https://github.com/intel-iot-devkit/safety-gear-detector-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect safety gear and generates detected image frames as a tar file (URI: /safetygeardetector/v1/detect) <br>

Safety Gear Detector Interface 
----------------
<h4>1. Detect safety gears </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /safetygeardetector/v1/detect <br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | video mp4 file   | Yes |

Return Parameters:

    TAR file containing detected images

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/safetygeardetector/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@Safety_Full_Hat_and_Vest.mp4;type=video/mp4'
```