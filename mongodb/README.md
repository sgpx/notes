# mongodb

## setup

```bash
sudo apt install -y mongodb
sudo echo BIND_IP = 172.31.0.2 > /etc/mongodb.conf
sudo echo PORT = 9999 >> /etc/mongodb.conf
sudo systemctl restart mongodb.service
```
