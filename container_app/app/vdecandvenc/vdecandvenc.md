VdecandVenc
==============
This is an application to encode a video by calling the venc and vdec APIs of the DVPP.<br>
This application is developed based on ascend project [vdecandvenc](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/0_data_process/vdecandvenc)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. <br>

Usage Steps:
--------------
Step 1: Provide input (mp4 file) for encoded and obtain output-id (URI: /ascend/v1/vdecandvenc/input) <br>
Step 2: Get output video (H.264 file) with the given output id (URI: /ascend/v1/vdecandvenc/output/{outputId})


VdecandVenc Interface 
----------------
<h4>1. Input video file</h4>
Input video file and obtain the output-id <br>

Resource URI: /ascend/v1/vdecandvenc/input<br>
Method: POST<br>

Request parameters:

None

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| video   | file                      | mp4 file    | Yes |

Example Request:

```
POST http://{{MEP_IP}}:{{PORT}}/ascend/v1/vdecandvenc/input
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| outputId     | string                     | Output Id to get the file later                  |

Return Code: 200 OK

Example Response:
```
HTTP/1.1 200 OK
{
    "outputId": "e0d7058c8080345569679df0a172a9cd"
}
```

Exception status code

| HTTP Status Code | Description |
| --- | --- |
| 400  | Bad request, used to indicate that the requested parameters are incorrect. |

<h4>2. Output video file</h4>
Output video file with output-id<br>

Resource URI: /ascend/v1/vdecandvenc/output/{outputId}<br>
Method: GET<br>

Request parameters:

None

Body parameters:

None

Example Request:

```
GET http://{{MEP_IP}}:{{PORT}}/ascend/v1/vdecandvenc/output/e0d7058c8080345569679df0a172a9cd
```

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| file     | file                     | output file                |

Return Code: 200 OK

Example Response:
```
HTTP/1.1 200 OK
<<File output>>
```
Exception status code

| HTTP Status Code | Description |
| --- | --- |
| 404  | resource not found. |

