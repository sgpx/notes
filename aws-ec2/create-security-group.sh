#!/bin/bash
vpc_id="vpc-XXXXX"
echo "enter group name"
read group_name
echo "enter group description"
read group_desc

group_id=$(aws ec2 create-security-group --group-name group_name --description group_desc --vpc-id $vpc_id | jq '.GroupId')

echo enter port number
read port_number

aws ec2 authorize-security-group-ingress --group-id $group_id --protocol tcp --port $port_number --cidr 0.0.0.0/0
