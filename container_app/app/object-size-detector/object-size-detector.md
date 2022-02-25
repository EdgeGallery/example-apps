Object Size Detector
---------------
This application demonstrates how to use CV to detect and measure the approximate size of assembly line parts. It is designed to work with an assembly line camera mounted above the assembly line belt. The application monitors mechanical parts as they are moving down the assembly line and raises an alert if it detects a part on the belt outside a specified size range.<br>
This application is developed based on open source project [Object Size Detector](https://github.com/intel-iot-devkit/object-size-detector-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect and measure the approximate size of assembly line parts and generates detected image frames as a tar file (URI: /objectSizeDetector/v1/detect) <br>

Object Size Detector Interface 
----------------
<h4>1. Detects and measure the approximate size of assembly line parts </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /objectSizeDetector/v1/detect <br>
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
  'http://127.0.0.1:8000/objectSizeDetector/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@bolt-multi-size-detection.mp4;type=video/mp4'
```