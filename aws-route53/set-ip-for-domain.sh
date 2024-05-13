#!/bin/bash
clear

echo enter domain
read domain

pushd ~/prog/notes/aws-route53
bash route53-list-zones.sh
popd

pushd ~/prog/notes/aws-ec2
bash get-instance-ips.sh
popd

echo enter zone id
read hosted_zone_id

echo ip address
read ip_addr

cd ~
cp -v prog/notes/aws-route53/example.json ~/a.json

sed -i.bak -r "s/foo.bar.com/$domain/g" a.json
sed -i.bak -r "s/1.2.3.4/$ip_addr/g" a.json

cat a.json

aws route53 change-resource-record-sets --hosted-zone-id $hosted_zone_id --change-batch file://a.json
