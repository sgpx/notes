#!/bin/bash
sudo certbot renew

cd axyz
rm -v *
pwd

cert_location="/path/to/mongo.pem"
mysubdomain="xyz.abc.com"
xpath="/etc/letsencrypt/live/$mysubdomain/"

a=$(sudo ls $xpath)

for i in $a; do
        echo $i;
        target=$(echo $xpath$(sudo readlink $xpath/$i));
        echo $target;
        sudo cp -v $target .
done

sudo chown ubuntu *
cat fullchain*pem >> mongo.pem
cat privkey*pem >> mongo.pem

cp -v mongo.pem 
rm -v *

cd $db_location
pwd

bash stop.sh
rm -v nohup.out
bash run-auth.sh
