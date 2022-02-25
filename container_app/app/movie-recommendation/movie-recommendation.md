Movie Recommendation
---------------
Recommendation engines are one of the most well known, widely used and highest value use cases for applying machine learning. This application is to get recommedations for movies with movie name.<br>
This application is developed based on open source project [elasticsearch-spark-recommender](https://github.com/IBM/elasticsearch-spark-recommender)<br>
REST APIs are additionally developed as part of this application for consumption by other producer applications running in MEC edge platform.<br>

Usage Steps:
--------------
Step 1: Provide movie name (text format) and number of prediction (as text format) and obtain output-ids (URI: /recommender/v1/input) <br>
Step 2: Get top n movie recommendation (text format) with the output-ids (URI: recommender/v1/input?id={outputId}) <br>

Movie recommendation Interface 
----------------
<h4>1. Movie recommendation input</h4>
Input image file and generates output-id <br>

Resource URI: /recommender/v1/input<br>
Method: POST<br>

Body Parameters:

| Name          | Type                        | Description              | Required      |
| ------------- | --------------------------- | ------------------------ | ------------- |
| movie    | text                      | movie name   | Yes |
| limit    | text                      | number recommedations required | Yes |

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| outputId     | string                     | outputId of the request. Will be used for getting recommendations|

Example Request:

```
curl -X 'POST'
  'http://{{HOST_IP}}:{{PORT}}/recommender/v1/input'
  -H 'accept: \*/\*'
  -H 'Content-Type: multipart/form-data'
  -F 'movie=matrix'
  -F 'limit=5'
```

Example Response:

```
HTTP/1.1 200 OK
{
    "outputId": "e0d7058c8080345569679df0a172a9cd"
}
```

<h4>2. Movie recommendation output</h4>
Generate top n movie <br>

Resource URI: recommender/v1/input?id={outputId}<br>
Method: GET<br>

Return Parameters:

| Name          | Type                        | Description              |
| ------------- | --------------------------- | ------------------------ |
| recommedations     | string                     | html embedded string with movie recommedations                  |

Example Request:

```
curl -X 'GET'
  'http://{{HOST_IP}}:{{PORT}}/recommender/v1/input?id=e0d7058c8080345569679df0a172a9cd'
  -H 'accept: \*/\*'
```

Example Response:

```
HTTP/1.1 200 OK
{
    "Recommendations": "<h2>Get similar movies for:</h2><h4>Matrix, The</h4><img src=https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg width=150></img><br><h2>People who liked this movie also liked these:</h2><table border=0><td><h5>Batman</h5><img src=https://image.tmdb.org/t/p/w500/tDexQyu6FWltcd0VhEDK7uib42f.jpg width=150></img></td><td><h5>1.959</h5></td><td><h5>Lethal Weapon</h5><img src=https://image.tmdb.org/t/p/w500/fTq4ThIP3pQTYR9eDepsbDHqdcs.jpg width=150></img></td><td><h5>1.957</h5></td><td><h5>Departed, The</h5><img src=https://image.tmdb.org/t/p/w500/kWWAt2FMRbqLFFy8o5R4Zr8cMAb.jpg width=150></img></td><td><h5>1.954</h5></td><td><h5>Snatch</h5><img src=https://image.tmdb.org/t/p/w500/56mOJth6DJ6JhgoE2jtpilVqJO.jpg width=150></img></td><td><h5>1.950</h5></td><td><h5>Thirteen</h5><img src=https://image.tmdb.org/t/p/w500/ey4injV5ZmIhiRFwsx9Ozh955Ir.jpg width=150></img></td><td><h5>1.949</h5></td></tr><tr></tr></table>"
}
```