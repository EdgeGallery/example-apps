Ai Paint
---------------
This is an application to teach machines to paint like human painters, who can use a small number of strokes to create fantastic paintings. By employing a neural renderer in model-based Deep Reinforcement Learning (DRL), our agents learn to determine the position and color of each stroke and make long-term plans to decompose texture-rich images into strokes. Experiments demonstrate that excellent visual effects can be achieved using hundreds of strokes. The training process does not require the experience of human painters or stroke tracking data.<br>
This application is developed based on open source project [ICCV2019-LearningToPaint](https://github.com/megvii-research/ICCV2019-LearningToPaint)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform. The API provided by this application could be used by other consumer application like gaming, social networking, teaching etc. <br>

Usage Steps:
--------------
<h4> Ai paint takes image</h4>
Step 1: Provide input (image file) for paint and obtain output-id (URI: /aipaint/v1/input) <br>
Step 2: Get output video with the given output id (URI: /aipaint/v1/output/{outputId})

Ai Paint Interface 
----------------
<h4>1. Input image file</h4>
Input the image file and obtain the output-id <br>

Resource URI: /aipaint/v1/input<br>
Method: POST<br>

Body Parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| image    | file                      | image file   | Yes |

Example Request:

```
curl -X 'POST'
  'http://{{HOST_IP}}:{{PORT}}/aipaint/v1/input'
  -H 'accept: application/json'
  -H 'Content-Type: multipart/form-data'
  -F 'image=@2.jpg;type=image/jpeg'
```

Example Response:

```
HTTP/1.1 200 OK
{
    "outputId": "e0d7058c8080345569679df0a172a9cd"
}
```

<h4>2. Output video file</h4>
Output video file with output-id<br>

Resource URI: /aipaint/v1/output/{outputId}<br>
Method: GET<br>

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| file     | file                     | output file                |

Example Request:

```
curl -X 'GET'
  'http://{{HOST_IP}}:{{PORT}}/aipaint/v1/output/e0d7058c8080345569679df0a172a9cd'
  -H 'accept: application/json'
```

Example Response:

```
HTTP/1.1 200 OK
<<File output>>
```
