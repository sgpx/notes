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
