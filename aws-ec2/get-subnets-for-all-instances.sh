#!/bin/bash
aws ec2 describe-instances --region ap-south-1 --query 'Reservations[].Instances[].[InstanceId, SubnetId]' --output table
