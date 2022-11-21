# netstat

network statistics and info

# installing

`apt install -y net-tools`

# routes

```
# netstat -r
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         10.88.0.1       0.0.0.0         UG        0 0          0 eth0
10.88.0.0       0.0.0.0         255.255.0.0     U         0 0          0 eth0
```

# interfaces

```
# netstat -i
```

# `netstat -tlpn`

`-t` => tcp sockets
`-l` => listening sockets
`-n` => don't resolve names
`-p` => list programs with PID
