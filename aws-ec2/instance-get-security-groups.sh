#!/bin/bash
aws ec2 describe-instances --instance-ids "$1" | jq -r '.Reservations[].Instances[].SecurityGroups[] | .GroupId'
