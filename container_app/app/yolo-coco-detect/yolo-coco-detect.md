YOLOV3 Coco Detection Video
==============
This is an application which detect objects that appear in the video and provide prediction results in the video.<br>
This application is developed based on ascend project [YOLOV3_coco_detection_video](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/2_object_detection/YOLOV3_coco_detection_video)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (mp4 file) to perform detection an objects and obtain the status of file input (URI: /ascend/v1/cocoDetectVideo/input) <br>


YOLOV3 Coco Detection Video Interface 
----------------
<h4>1. Input video file</h4>
Input video file and obtain the status of file <br>

Resource URI: /ascend/v1/cocoDetectVideo/input<br>
Method: POST<br>

Request parameters:

None

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| video    | file                      | mp4 video file      | Yes |

Example Request:

```
POST http://{{MEP_IP}}:{{PORT}}/ascend/v1/cocoDetectVideo/input
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| result     | string                     | successfully run                  |

Return Code: 200 OK

Example Response:
```
HTTP/1.1 200 OK
{
    "result": "Ok"
}
```

Exception status code

| HTTP Status Code | Description |
| --- | --- |
| 400  | Bad request, used to indicate that the requested parameters are incorrect. |


