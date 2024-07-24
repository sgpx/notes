#!/bin/bash
clear

if [ "$1" = "" ]; then
	echo enter domain
	read domain
else
	domain="$1"
        root=$(sed -r "s/^(.+\.)*(.+)\.(.+)$/\2\.\3/" <<< "$1")
	echo $root
fi


if [ "$2" = "" ]; then
	pushd ~/prog/notes/aws-route53
	IFS=$'\n'
	hxid=$(bash route53-list-zones.sh | grep "$root" | head -n1 | sed -r "s/(.+) ### (.+)\.$/\1/")
	echo $hxid
	popd
	hosted_zone_id="$hxid"
else
	hosted_zone_id="$2"
fi

if [ "$3" = "" ]; then
	pushd ~/prog/notes/aws-ec2
	bash get-instance-ips.sh
	echo ip address
	read ip_addr
else
	ip_addr="$3"
fi


cd ~
cp -v ~/prog/notes/aws-route53/example.json ~/tmp.json

sed -i.bak -r "s/foo.bar.com/$domain/g" tmp.json
sed -i.bak -r "s/1.2.3.4/$ip_addr/g" tmp.json

cat tmp.json

cx=$(aws route53 change-resource-record-sets --hosted-zone-id $hosted_zone_id --change-batch file://tmp.json)
cxid=$(echo $cx | jq -r '.ChangeInfo.Id')
echo $cxid
rm tmp.json

st=$(aws route53 get-change --id $cxid | jq -r '.ChangeInfo.Status')

while [ "$st" != "INSYNC" ]; do
	st=$(aws route53 get-change --id $cxid | jq -r '.ChangeInfo.Status')
	echo $st
done

