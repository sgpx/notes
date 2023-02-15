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
