Object Flaw Detector
---------------
The object flaw detector application detects the anomalies such as color, crack, and orientation of the object moving on a conveyor belt. Anomalies are marked as defective and saved in the color, crack, orientation folders respectively. Also objects with no defects are saved in no_defect folder. These anomalies data is sent to InfluxDB* database and is visualized on Grafana*. This application also measures length and width of the object in millimeters.<br>
This application is developed based on open source project [Object Flaw Detector](https://github.com/intel-iot-devkit/object-flaw-detector-python) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide input video to detect flaws in the object and generates detected image frames as a tar file including per defect category (orientation, crack, color, no_defect) folder (URI: /objectflawdetector/v1/detect) <br>
Additionally results can be viewed in Graphana for which configurations can be found at [Object Flaw Detector](https://github.com/intel-iot-devkit/object-flaw-detector-python)

Object Flaw Detector Interface 
----------------
<h4>1. Detects orientation, crack & color defect in an object </h4>
Input (video file) and obtain detected images. <br>

Resource URI: /objectflawdetector/v1/detect <br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | video mp4 file   | Yes |

Return Parameters:

    TAR file containing detected images in folders per defect category (orientation, crack, color) & a no defect folder.

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/objectflawdetector/v1/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@bolt-detection.mp4;type=video/mp4'
```