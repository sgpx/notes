# lsof

## find open ports

```
$ lsof -i -n -P | grep -i 3000
Python    73545   sp    3u  IPv4 0x6cb67f53e16ce828      0t0  TCP 127.0.0.1:3000 (LISTEN)
```

## find open ports

```
$ lsof -i -P | grep 5000
gvproxy   16596   sp   20u  IPv6 0xa60cc82238fd8b9f      0t0  TCP *:5000 (LISTEN)
```
