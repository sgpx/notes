#!/bin/bash
aws ec2 describe-instances | jq -r '.Reservations[].Instances[] | .InstanceId + " # "  + .NetworkInterfaces[].Association.PublicIp + " # " + (.Tags.[] | .Value)'
