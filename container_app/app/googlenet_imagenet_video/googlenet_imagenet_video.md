Googlenet Classify
==============
This is an application uses the googlenet_imagenet  model to perform classification inference on the input videos.<br>
This application is developed based on ascend project [googlenet_imagenet_video](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/googlenet_imagenet_video)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (mp4 file) to perform classification inference and obtain the status of file input (URI: /ascend/v1/googlenetClassify/input) <br>
Step 2: Delete input file and obtain the status of sucessfully deletion of input file (URI: /ascend/v1/googlenetClassify/input)


Googlenet Classify Interface 
----------------
<h4>1. Input video file</h4>
Input video file and obtain the status of file <br>

Resource URI: /ascend/v1/googlenetClassify/input<br>
Method: POST<br>

Request parameters:

None

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| video    | file                      | mp4 video file      | Yes |

Example Request:

```
POST http://{{MEP_IP}}:{{PORT}}/ascend/v1/googlenetClassify/input
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

Resource URI: /ascend/v1/googlenetClassify/input<br>
Method: DELETE<br>

Request parameters:

None

Body parameters:

None

Example Request:

```
DELETE http://{{MEP_IP}}:{{PORT}}/ascend/v1/googlenetClassify/input
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

