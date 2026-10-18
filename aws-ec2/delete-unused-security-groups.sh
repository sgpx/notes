#!/bin/bash
grp=$(bash get-all-security-groups.sh | sed -r "s/default # .+//g" | sed -r "s/(.+) # (.+) # (.+)/\2/" | grep -E ".+")
sg=$(bash get-security-groups-for-all-instances.sh) 

for i in $grp; do
	exists=$(echo $sg | grep $i)
	if [ "$exists" = "" ]; then 
		echo $i is unused, deleting..
		aws ec2 delete-security-group --group-id $i
	fi
done
