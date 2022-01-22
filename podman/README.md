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

# list networks

```
NETWORK ID    NAME        VERSION     PLUGINS
XXXXXXXXXXX  podman      0.4.0       bridge,podman-machine,portmap,firewall,tuning
```

# check network

```
podman network inspect podman
```

