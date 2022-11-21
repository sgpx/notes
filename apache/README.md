# setup (container, without systemd)

```
apt install -y apache2
sed -i .bak -r "s/Listen 80/Listen 5000/" /etc/apache2/ports.conf
echo "ServerName 10.88.0.2" >> /etc/apache2/sites-available/000-default.conf

useradd apacheuser
groupadd apachegroup

usermod -G apachegroup apacheuser

mkdir /home/apacheuser
mkdir /home/apacheuser/apache-run-dir/
mkdir /home/apacheuser/apache-log-dir/
usermod -m -d /home/apacheuser apacheuser

chown apacheuser /home/apacheuser
chown apacheuser /home/apacheuser/*

cd /home/apacheuser

su -c 'cd /home/apacheuser && APACHE_RUN_DIR="$PWD/apache-run-dir/" APACHE_RUN_USER="apacheuser" APACHE_RUN_GROUP="apachegroup" APACHE_LOG_DIR="$PWD/apache-log-dir/" APACHE_PID_FILE="$PWD/apache.pidfile" apache2' apacheuser 
```


# increase request size limit


```
sudo echo "LimitRequestBody 99999999" >> /etc/apache2/apache2.conf
sudo systemctl restart apache2
```
