#!/bin/bash
region="us-east-1"

if [ "$1" != "" ]; then
	region="$1"
fi
echo region is $region
aws ec2 describe-instances --region $region | jq '.Reservations | map (.Instances) | .[] | map (.PublicIpAddress)'
