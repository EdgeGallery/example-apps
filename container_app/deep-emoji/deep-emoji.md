Deep Moji
===
This repo is used to develop an app based on osdt mep
-----
This is an application for predicting the top 5 emojis.  The service was developed on the basis of an open project for deep emoji on Github. The project is characterized by the following：

This application exposes only two rest API. In one of the rest interface, it takes text as an input and produces the top 5 emoji classes as an output and it's the confidence interval.

If someone wants an image of a particular class image then the second rest interface help. It takes the class number as an input and returns the png file of the emoji as output.

Exposed API
===
Get top 5 classes of an emoji
-------
It takes text as an input and produce top 5 emoji classes as an output and it's confidence interval. <br>
restful API ：POST http://127.0.0.1:30097/deepmoji/v1/input<br>
input：Text whose emoji to be predicted<br>
curl -X 'POST' \
  'http://127.0.0.1:31651/deepmoji/v1/input' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=This%20is%20the%20shit!'<br>
  
Image of emoji
-----------
It takes class number as an input and return the png file of the emoji as output. <br>
restful API ：POST http://127.0.0.1:30097/deepmoji/v1/getmoji<br>
input：Class between 0 - 63 for which emoji image to be detected. <br>
curl -X 'POST' \
  'http://127.0.0.1:31651/deepmoji/v1/getmoji' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'class=27'
