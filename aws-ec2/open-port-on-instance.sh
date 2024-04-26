#!/bin/bash
cd ~/prog/notes/aws-ec2
bash get-instance-vpcs.sh

echo "enter instance id"
read instance_id
vpc_id=$(bash instance-get-vpc.sh "$instance_id")
echo enter port number
read port_number

ts=$(date +%s)
group_name="testgrp_$ts_$port_number"
group_desc="$group_name_port_$port_number"

echo making group $group_name

group_id=$(aws ec2 create-security-group --group-name $group_name --description $group_desc --vpc-id $vpc_id | jq -r '.GroupId')

aws ec2 authorize-security-group-ingress --group-id $group_id --protocol tcp --port $port_number --cidr 0.0.0.0/0

prev_groups=$(bash instance-get-security-groups.sh $instance_id)

aws ec2 modify-instance-attribute --instance-id $instance_id --groups $group_id $prev_groups

bash instance-get-security-groups.sh $instance_id
