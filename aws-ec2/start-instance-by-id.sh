#!/bin/bash
if [ "$1" = "" ]; then
	bash get-instance-vpcs.sh
	read inst
else
	inst="$1"
fi

echo starting instance $inst
aws ec2 start-instances --instance-ids "$inst"
st=$(aws ec2 describe-instances --instance-ids $inst | jq -r '.Reservations[0].Instances[0].State.Name')

while [ "$st" != "running" ]; do
	echo waiting.. $st
	st=$(aws ec2 describe-instances --instance-ids $inst | jq -r '.Reservations[0].Instances[0].State.Name')
	sleep 5
done
