# https

first, set a DNS `A` record that points to IP address of the server

```
$ dig my.website.com

my.website.com.	300	IN	A	7.8.9.10

```

then, on the server

```
sudo hostnamectl set-hostname my.website.com
sudo apt install -y apache2
sudo snap install certbot --classic
sudo certbot
```
