auto adjust system clock from network

```bash
apt install -y ntp
cp /usr/share/zoneinfo/Asia/Singapore /etc/localtime
ntpd start
```
