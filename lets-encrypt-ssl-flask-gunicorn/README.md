# https with gunicorn and lets encrypt

# setup

`sudo apt install -y python3-pip openssl`

`sudo pip3 install gunicorn flask flask_cors pymongo`

`sudo snap install certbot --classic`

# set server hostname

`sudo hostnamectl set-hostname foo.example.com`

# point DNS A record to server IP

`A foo.example.com 1.2.3.4`

# get certificates from certbot

`sudo certbot certonly -d foo.example.com --config-dir certbot_config_dir/ --work-dir certbot_work_dir/ --logs-dir certbot_logs_dir/`

# copy certificates

use `chown`

```
mkdir certdir
cp certbot_config_dir/live/foo.example.com/*.pem certdir
```

# start server

as root (needed for acces to port 80 and 443)

`nohup gunicorn app:app -w 10 --certfile=certdir/cert.pem --keyfile=certdir/privkey.pem --bind 0.0.0.0:443 &`
