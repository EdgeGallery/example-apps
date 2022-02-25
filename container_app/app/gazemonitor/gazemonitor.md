Shopper Gaze Monitor
---------------
This shopper gaze monitor application is designed for a retail shelf mounted camera system that counts the number of passers-by and the number of people who look towards the display. It is intended to provide real-world marketing statistics for in-store shelf-space advertising.<br>
This application is developed based on open source project [Shopper Gaze Monitor](https://github.com/intel-iot-devkit/shopper-gaze-monitor-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect whether shopper is looking at monitor and generates detected image frames as a tar file (URI: /gazemonitor/v1/detect) <br>

Shopper Gaze Monitor Interface 
----------------
<h4>1. Detects whether shopper is looking at monitor </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /gazemonitor/v1/detect <br>
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
  'http://127.0.0.1:8000/gazemonitor/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@face-demographics-walking-and-pause.mp4;type=video/mp4'
```