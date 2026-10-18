#!/bin/bash
username="apache_user"

apt update
apt install -y apache2 apache2-utils nano curl libexpat1 sudo python3 python3-pip

groupadd $username
useradd $username
usermod -a -G $username $username

# usermod -a -G sudo $username
# printf "$username\tALL=(ALL:ALL) ALL" >> /etc/sudoers

# su -c "apache2ctl start" $username

apache2ctl start
