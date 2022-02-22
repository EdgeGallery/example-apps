Yunex car plate recognition app
===
This repo is used for develop app based on osdt mep
-----
This is an app application for car plate recognition microservices. This app is developed by
Yunex company and can be used to recognize car plate picture.

Features
===
car plate recognition
------

### start the instance

```
root@exsight:~# docker run -d -p 8080 edgegallery/yunex:latest     
ca499dc4d3b0dad9d2d6bd4f904b49f8767dcf0bf3463876258f05b55f082cdb

root@exsight:~# docker ps
CONTAINER ID        IMAGE                      COMMAND                  CREATED              STATUS              PORTS                     NAMES
ca499dc4d3b0        edgegallery/yunex:latest   "/usr/sbin/entrypoin…"   4 seconds ago        Up 2 seconds        0.0.0.0:32769->8080/tcp   zealous_murdock
```
### health check

```
root@exsight:~# curl localhost:32769/api/hi

{

  "code": 0,

  "message": "hello, world!"

}
```

### log in

```
root@exsight:~# curl localhost:32769/api/login -XPOST -d '{"username":"admin", "password":"admin@yunex.com"}'

{

  "code": 0,

  "message": "login success",

  "results": {

    "token": "KYN83VH8SFZJ3JaS5MOa7IG1HIB2X6SY"

  }

}root@exsight:~# 

root@exsight:~# export token=KYN83VH8SFZJ3JaS5MOa7IG1HIB2X6SY
```

### modify password

```
root@exsight:~# curl -H "YunEx-Token-ID: ${token}" localhost:32769/api/user -d '{"username":"admin", "password":"452a3cd9dcfe"}'  

{
  "code": 0,
  "message": "success"
}

root@exsight:~# 

root@exsight:~# curl localhost:32769/api/login -XPOST -d '{"username":"admin", "password":"admin@yunex.com"}'                   

{
  "code": 0,
  "message": "login failed"
}

root@exsight:~# curl localhost:32769/api/login -XPOST -d '{"username":"admin", "password":"452a3cd9dcfe"}'                                  

{
  "code": 0,
  "message": "login success",
  "results": {
    "token": "KO9MSERAV3XP6EZ3BHMHZFF99JMBIQQB"
  }

}root@exsight:~# 

root@exsight:~# export token=KO9MSERAV3XP6EZ3BHMHZFF99JMBIQQB
```

### car recognition

```
root@exsight:~# curl -H "YunEx-Token-ID: ${token}" localhost:32769/api/vehicle -F "image=@/opt/car/car3.jpg"

{
  "code": 0,
  "results": {
    "attribute": "white car",
    "license": "<Jiangsu>BD00008"
  }
}
```