First,make sure docker can pull the image from the mirror source 159.138.11.6:8089

modify daemon.json, file in etc/docker/daemon.json this directoy

Add the following code in daemon.json

"insecure-registries": [
    "159.138.11.6:8089"
  ]

then login docker:

docker login -u admin -p admin123 159.138.11.6:8089


Last:

kubectl create -f face_recogniton.yaml