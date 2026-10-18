#!/bin/bash
cd ~/prog/notes/aws-ec2
bash get-instance-vpcs.sh

echo "enter vpc id"
read vpc_id

echo using $vpc_id

echo "enter group name"
read group_name
echo "enter group description"
read group_desc

group_id=$(aws ec2 create-security-group --group-name $group_name --description $group_desc --vpc-id $vpc_id | jq -r '.GroupId')

echo enter port number
read port_number

aws ec2 authorize-security-group-ingress --group-id $group_id --protocol tcp --port $port_number --cidr 0.0.0.0/0


echo enter instance id
read instance_id

prev_groups=$(bash instance-get-security-groups.sh $instance_id)

aws ec2 modify-instance-attribute --instance-id $instance_id --groups $group_id $prev_groups

bash instance-get-security-groups.sh $instance_id
