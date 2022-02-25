Color a Video
==============
This is an application uses the colorization model to perform coloring inference on the input black and white videos.<br>
This application is developed based on ascend project [colorization_video](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/6_other/colorization_video)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (mp4 file) for colorizing a video from black and white video and obtain the status of file input (URI: /ascend/v1/colorizationVideo/input) <br>
Step 2: Delete input file and obtain the status of sucessfully deletion of input file (URI: /ascend/v1/colorizationVideo/input)


Color a Video Interface 
----------------
<h4>1. Input video file</h4>
Input video file and obtain the status of file <br>

Resource URI: /ascend/v1/colorizationVideo/input<br>
Method: POST<br>

Request parameters:

None

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| video    | file                      | mp4 video file  in black and white    | Yes |

Example Request:

```
POST http://{{MEP_IP}}:{{PORT}}/ascend/v1/colorizationVideo/input
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

Resource URI: /ascend/v1/colorizationVideo/input<br>
Method: DELETE<br>

Request parameters:

None

Body parameters:

None

Example Request:

```
DELETE http://{{MEP_IP}}:{{PORT}}/ascend/v1/colorizationVideo/input
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

