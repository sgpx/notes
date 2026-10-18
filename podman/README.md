# podman

daemonless container engine

# how it works

https://www.redhat.com/sysadmin/podman-mac-machine-architecture

# setup (macOS)

`brew install podman`

# pull image

`podman pull ubuntu`

# pull specific version of image (TAGS)

`podman pull ubuntu:16.04`

# setup VM

```
podman machine init
podman machine start
```

```
podman machine init $machineName
podman machine start $machineName
```

# stop VM

```
podman machine stop
```

```
podman machine stop $machineName
```

# run container in VM

```bash
podman pull ubuntu
podman run --name ubuntu1 -it -d ubuntu bash
podman exec -it ubuntu1 bash
``` 

# stop containers in VM

```bash
podman stop ubuntu1
```

# copy local files to container

```bash
podman cp a.txt ubuntu1:/root/a.txt
```

# get list of running containers

```
podman ps
podman ps -a # includes exited
podman ps -aq # quiet mode
```

# remove containers

```
podman stop $(podman ps -aq)
podman rm $(podman ps -aq)
```

# get list of downloaded images

```
podman images
```

```
bash-3.2$ podman images
REPOSITORY                           TAG            IMAGE ID      CREATED       SIZE
localhost/xyz                        latest         cf5994f8f2e5  31 hours ago  88.3 MB
docker.io/library/ubuntu             18.04          df8edc186894  4 weeks ago   58.9 MB
registry.fedoraproject.org/fedora    latest         b74713569c6a  2 months ago  174 MB
docker.io/library/ubuntu             latest         d5ca7a445605  3 months ago  68.1 MB
```

# remove an image

`podman rmi localhost/xyz`

# specify custom entrypoint for target image 

`podman run -it -d --entrypoint "/bin/busybox" alpine`

# build image from container files

```
$ ls 
Dockerfile
$ podman build --tag xyz .
$ podman run -d xyz
```
# list networks

```
NETWORK ID    NAME        VERSION     PLUGINS
XXXXXXXXXXX  podman      0.4.0       bridge,podman-machine,portmap,firewall,tuning
```

# check network

```
podman network inspect podman
```

# issues

error connection closed, etc => is gvproxy laggy?
