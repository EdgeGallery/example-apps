Bicycle GAN
---------------
It is Pytorch implementation for multimodal image-to-image translation. For example, given the same night image, our model is able to synthesize possible day images with different types of lighting, sky and clouds.<br>
This application is developed based on open source project [BicycleGAN](https://github.com/junyanz/BicycleGAN) <br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Provide image input (image file) and type (supported types: night2day, edges2handbags, edges2shoes, maps) to generate translated images (URI: /bicyclegan/v1/translate) <br>

Bicycle GAN Interface 
----------------
<h4>1. Translate Image</h4>
Input (image file) and type (supported types: night2day, edges2handbags, edges2shoes, maps) and obtain translated images. <br>

Resource URI: /bicyclegan/v1/translate<br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| file    | file                      | image file   | Yes |
| type    | text                      | supported types: night2day, edges2handbags, edges2shoes, maps | Yes |

Return Parameters:

    TAR file containing translated images with index.html

Example Request:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/bicyclegan/v1/translate' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@2_AB.jpg;type=image/jpeg' \
  -F 'type=edges2shoes'
```