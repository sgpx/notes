# ip

show network devices and routes

# setup

`apt install -y iproute2`

# args

`-c` => color output

`-4` => ipv4 only

`-6` => ipv6 only

# get ip addresses

`ip -c addr`

```
# ip -c addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 9e:ee:08:2c:9b:d6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.88.0.2/16 brd 10.88.255.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::9cee:8ff:fe2c:9bd6/64 scope link 
       valid_lft forever preferred_lft forever
```
