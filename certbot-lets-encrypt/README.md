# certbot

# install

`sudo snap install certbot --classic`

# setup

```
sudo hostnamectl set-hostname blah.com
sudo snap install --classic certbot
sudo apt install -y apache2 php
sudo certbot
```

# setup specific domain

`sudo certbot -d blah.com`

# get certificate status

`sudo certbot certificates`

# renew certs

`sudo certbot renew`

# use webroot

multiple domains :

`certbot -d mydomain.com,www.mydomain.com certonly --webroot --webroot-path /path/to/www/ --config-dir certbot-config --logs-dir certbot-logs --work-dir certbot-work`

# avoid letsencrypt cert chain not verified error

```
sudo certbot certonly -d mywebsite.com
sudo cp /etc/letsencrypt/live/mywebsite.com/fullchain.pem cert-
with-chain.pem
sudo cat /etc/letsencrypt/live/mywebsite.com/cert.pem >> cert-w
ith-chain.pem
```
