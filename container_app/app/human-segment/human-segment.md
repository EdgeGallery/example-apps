Segment of Human Figure
==============
This is an application uses semantic segmentation model to perform semantic segmentation inference on the human body in the input video.<br>
This application is developed based on ascend project [human_segmentation](https://gitee.com/ascend/samples/tree/master/cplusplus/contrib/human_segmentation)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (mp4 file) for human figure and obtain the status of file input (URI: /ascend/v1/humanSegment/input) <br>
Step 2: Delete input file and obtain the status of sucessfully deletion of input file (URI: /ascend/v1/humanSegment/input)


Segment of Human Figure Interface 
----------------
<h4>1. Input video file</h4>
Input video file and obtain the status of file <br>

Resource URI: /ascend/v1/humanSegment/input<br>
Method: POST<br>

Request parameters:

None

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| video    | file                      | mp4 video file    | Yes |

Example Request:

```
POST http://{{MEP_IP}}:{{PORT}}/ascend/v1/humanSegment/input
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

<h4>2. Delete video file</h4>
Delete video file and obtain the status of file deletion. <br>

Resource URI: /ascend/v1/humanSegment/input<br>
Method: DELETE<br>

Request parameters:

None

Body parameters:

None

Example Request:

```
DELETE http://{{MEP_IP}}:{{PORT}}/ascend/v1/humanSegment/input
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| result     | string                     |  successfully deleted                |

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
| 400  | Bad. |

