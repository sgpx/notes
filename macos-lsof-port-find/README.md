# lsof

## find open ports

```
$ lsof -i -P | grep 5000
gvproxy   16596   sp   20u  IPv6 0xa60cc82238fd8b9f      0t0  TCP *:5000 (LISTEN)
```
