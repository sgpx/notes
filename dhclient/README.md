# iwd ipv4 fix

```
device_id=wlan0
dhclient -4 -r $device_id
dhclient $device_id
```
