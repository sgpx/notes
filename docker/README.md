# docker

# build from dockerfile

```
$ ls
Dockerfile
$ docker build . --tag myreponame:mytag
$ docker build -f Dockerfile --tag myreponame:mytag
```

# docker save image to tar

```
$ docker image save myreponame -o my.tar && tar xf my.tar
```

# docker-compose

start containers

`sudo docker-compose up`

detached mode

`sudo docker-compose up -d` 

stop containers

`sudo docker-compose down`

