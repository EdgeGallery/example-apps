People Counter
---------------
The people counter application is one of a series of IoT reference implementations aimed at instructing users on how to develop a working solution for a particular problem. This solution detects people in a designated area, providing the number of people in the frame, average duration of people in frame, and total count.<br>
This application is developed based on open source project [People Counter](https://github.com/intel-iot-devkit/people-counter-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect people in a designated area, providing the number of people in the frame, average duration of people in frame, and total count and generates detected image frames as a tar file (URI: /peopleCounter/v1/detect) <br>

People Counter Interface 
----------------
<h4>1. Detects people in a designated area, providing the number of people in the frame, average duration of people in frame, and total count </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /peopleCounter/v1/detect <br>
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
  'http://127.0.0.1:8000/peopleCounter/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@bolt-multi-size-detection.mp4;type=video/mp4'
```