Easy OCR
---------------
It is ready to use OCR (optical character recognition) application with 80+ supported languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and etc.<br>
This application is developed based on open source project [EasyOCR](https://github.com/JaidedAI/EasyOCR)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>
Provided APIs could be consumed by multiple applications for use cases like <br>

- Data entry for business documents, e.g. Cheque, passport, invoice, bank statement and receipt
- Automatic number plate recognition (surveillance system)
- In airports, for passport recognition and information extraction
- Automatic insurance documents key information extraction
- Traffic sign recognition
- Extracting business card information into a contact list
- More quickly make textual versions of printed documents, e.g. book scanning for Project Gutenberg
- Make electronic images of printed documents searchable, e.g. Google Books
- Converting handwriting in real-time to control a computer (pen computing)
- Defeating CAPTCHA anti-bot systems, though these are specifically designed to prevent OCR. The purpose can also be to test the robustness of CAPTCHA anti-bot systems.
- Assistive technology for blind and visually impaired users
- Writing the instructions for vehicles by identifying CAD images in a database that are appropriate to the vehicle design as it changes in real time.
- Making scanned documents searchable by converting them to searchable PDFs

Usage Steps:
--------------
Step 1: Provide image input (image file) and language to generate text (URI: /ocr/v1/input) <br>

Easy OCR Interface 
----------------
<h4>1. OCR input</h4>
Input the image file as well as the language and obtain text <br>

Resource URI: /ocr/v1/input<br>
Method: POST<br>

Body parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| image    | file                      | image file   | Yes |
| langs    | text                      | languages supported  in the image to be extracted (Language Code with space) | Yes |

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| output     | string                     | Extracted text from image along with their coordinates                  |

Example Request:

```
curl -X 'POST'
  'http://{{HOST_IP}}:{{PORT}}/ocr/v1/input'
  -H 'accept: application/json'
  -H 'Content-Type: multipart/form-data'
  -F 'image=@12.png;type=image/png'
  -F 'langs=en'
```

Example Response:

```
HTTP/1.1 200 OK
{
    "outputId": "([[86, 80], [134, 80], [134, 128], [86, 128]], '?', 0.6629598563364745)\n([[189, 75], [469, 75], [469, 165], [189, 165]], '???', 0.9619015323198089)\n([[517, 81], [565, 81], [565, 123], [517, 123]], '?', 0.9935730580773452)\n([[78, 126], [136, 126], [136, 156], [78, 156]], '315', 0.999992910975279)\n([[514, 126], [574, 126], [574, 156], [514, 156]], '309', 0.9999620084121807)\n([[79, 173], [125, 173], [125, 213], [79, 213]], 'W', 0.23369882903558903)\n([[226, 170], [414, 170], [414, 220], [226, 220]], 'Yuyuan Rd?', 0.8949639433306373)\n([[529, 173], [569, 173], [569, 213], [529, 213]], 'E', 0.5179029432256108)\n
}
```