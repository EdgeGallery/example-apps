Cherry
===
This repo is used to develop an app based on osdt mep
-----
This is an application for a movie review's rating. The service was developed on the basis of an open project for the cherry on Github. The project is characterized by the following：

This application exposes only one rest API in which sentence has to be uploaded and in response, it will give the rating and its confidence interval as output.

Exposed API
===
Sentence upload
-------
The sentence is given as an input and in return it will give the rating and it's confidence interval as output. <br>
restful API ：POST http://127.0.0.1:30096/cherry/v1/input<br>
Support multiple faces for comparison<br>
input：Movie review complete sentence whose rating to be predicted. <br>
curl -X 'POST' \
  'http://127.0.0.1:30096/cherry/v1/input' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=This%20is%20an%20extremely%20entertaining%20and%20often%20insightful%20collection%20by%20Nobel%20physicist%20Richard%20Feynman%20drawn%20from%20slices%20of%20his%20life%20experiences.%20Some%20might%20believe%20that%20the%20telling%20of%20a%20physicist'\''s%20life%20would%20be%20droll%20fare%20for%20anyone%20other%20than%20a%20fellow%20scientist%2C%20but%20in%20this%20instance%2C%20nothing%20could%20be%20further%20from%20the%20truth.'<br>

