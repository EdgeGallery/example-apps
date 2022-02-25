Restricted Zone Notifier
---------------
This application is designed to detect the humans present in a predefined selected assembly line area. If the people enters the marked assembly area, it raises the alert and sends through mqtt.<br>
This application is developed based on open source project [Restricted Zone Notifier](https://github.com/intel-iot-devkit/restricted-zone-notifier-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect the humans present in a predefined selected assembly line area and generates detected image frames as a tar file (URI: /restrictedZoneNotifier/v1/detect) <br>

Restricted Zone Notifier Interface 
----------------
<h4>1. Detects the humans present in a predefined selected assembly line area </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /restrictedZoneNotifier/v1/detect <br>
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
  'http://127.0.0.1:8000/restrictedZoneNotifier/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@bolt-multi-size-detection.mp4;type=video/mp4'
```