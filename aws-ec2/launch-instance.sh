#!/bin/bash

echo enter instance type 
read INSTANCE_TYPE

echo enter AMI ID
read IMAGE_ID

echo enter ebs size
read EBS_SIZE

echo enter key name
read KEY_NAME

echo enter security group
read SECURITY_GROUP

echo enter subnet
read SUBNET_ID

INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $IMAGE_ID \
    --count 1 \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $SECURITY_GROUP \
    --block-device-mappings "[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"VolumeSize\":$EBS_SIZE}}]" \
    --query 'Instances[0].InstanceId' \
    --output text)


echo $INSTANCE_ID
