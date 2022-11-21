#!/bin/bash
aws ec2 describe-instances | jq '.Reservations[0].Instances[0].NetworkInterfaces[0].PrivateIpAddresses[0].Association.PublicIp'
