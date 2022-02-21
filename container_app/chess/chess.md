# Docker-Chess

Let's run the Chess PHP App using Docker. These steps assume that you are using a Mac.

Make sure you have Docker installed and running on your Mac and follow the steps below:

```
cd /work
git clone https://github.com/rm511130/docker-chess
cd docker-chess
docker build . -t chess
docker run -d --rm -p 8080:80 chess
```

Access the Chess App using a browser: http://127.0.0.1:8080

![](./chess.jpg)

To stop the Docker Chess program, follow this example:

```
docker ps

CONTAINER ID   IMAGE  COMMAND                  CREATED              STATUS              PORTS                 NAMES
1eaebd33e42b   chess  "docker-php-entrypoi…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp  pedantic_yalow

docker stop 1eaebd33e42b
```

# Pushing our Docker image of Chess to the Docker Hub

These are the steps I executed to upload the Docker Chess App image from my Mac to my Docker Hub repo:

```
docker image tag chess rmeira/chess
docker push rmeira/chess
```

You can now run Docker Chess using the following command. Note that the `rmeira/chess` reference indicates that the Docker-Chess Image will be pulled from Docker Hub.

```
docker run -d -p 8080:80 rmeira/chess
```

And access the Chess App using a browser: http://127.0.0.1:8080


# Running Docker-Chess on a Kubernetes Cluster

## Example 1

In the example below, I used a [TKGI](https://docs.vmware.com/en/VMware-Tanzu-Kubernetes-Grid-Integrated-Edition/index.html) K8s cluster that was previously created on GCP. The name of the cluster is `large` and the TKGI provisioning environment knows how to spin up GCP Load Balancers when you issue a `kubectl` command to expose a service of `--type=LoadBalancer`.

```
tkgi get-credentials large
kubectl create deployment chess --image=rmeira/chess 
kubectl expose deployment chess --port=80 --target-port=80 --name=chess --type=LoadBalancer
kubectl get service chess
```

You should see an output that looks like this:

```
NAME    TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
chess   LoadBalancer   10.100.200.34   34.74.197.59   80:32238/TCP   39s
```

Take the `External-IP` address of the `LoadBalancer` and use the `open` command to open a browser as shown below:

```
open http://34.74.197.59 
```

![](./images/docker-chess.png)

## Example 2

In the example below, I used a [TKGI](https://docs.vmware.com/en/VMware-Tanzu-Kubernetes-Grid-Integrated-Edition/index.html) K8s cluster that was previously created on vSphere without NSX-T. The name of the cluster is `small` and I opted to expose a `chess` service of `--type=NodePort`.

Let's first target the TKGI API so we can request the `kubeconfig` credentials for the `small` K8s cluster:

```
tkgi login -a https://api.pks.pcf4u.com:9021 -u pks_admin -p password -k
```

You should see the following output:

```
API Endpoint: https://api.pks.pcf4u.com:9021
User: pks_admin
Login successful.
```

Now we can proceed as follows:

```
tkgi get-credentials small
kubectl create deployment chess --image=rmeira/chess 
kubectl expose deployment chess --port=80 --target-port=80 --name=chess --type=NodePort
kubectl get service chess
```

You should see an output that looks like this:

```
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
chess   NodePort   10.100.200.56   <none>        80:30438/TCP   7s
```

You'll need the IP address of one of the Worker Nodes of the `small` cluster. Execute the following command:

```
kubectl get nodes -o wide
```

You should see an output that looks like this:

```
NAME                                 STATUS ROLES   AGE   VERSION            INTERNAL-IP   EXT-IP     OS-IMAGE             KERNEL-VERSION       CONTAINER-RUNTIME
167e6455-7686-4c2b-aba1-e418ecfc928b Ready  <none>  19d   v1.19.6+vmware.1   10.0.7.17     10.0.7.17  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
1e036a19-09ed-43d1-8403-52892b5bd83a Ready  <none>  20d   v1.19.6+vmware.1   10.0.7.15     10.0.7.15  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
2afe6614-30b8-4449-bf83-1647bcae59ff Ready  <none>  20d   v1.19.6+vmware.1   10.0.7.14     10.0.7.14  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
779e9b16-4e82-438e-9258-d8ee2cfec074 Ready  <none>  20d   v1.19.6+vmware.1   10.0.7.11     10.0.7.11  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
9030e7db-e4db-4124-872f-cf48f8c39d58 Ready  <none>  20d   v1.19.6+vmware.1   10.0.7.16     10.0.7.16  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
b9a17e95-1b1d-40f9-b6d3-39e533969904 Ready  <none>  20d   v1.19.6+vmware.1   10.0.7.12     10.0.7.12  Ubuntu 16.04.7 LTS   4.15.0-133-generic   docker://19.3.14
```

Take any `External-IP` address of a Worker Node, for example `10.0.7.17`, and use port `30438` which can be found in the output of the `kubectl get service` command. 

Now open a browser per the example below:

```
open http://10.0.7.17:30438
```

_Le voilà!_

![](./images/chess-v2.png)


