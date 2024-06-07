#!/bin/bash
aws ec2 describe-security-groups | jq -r '.SecurityGroups[] | .GroupName + " # " + .GroupId + " # " + .OwnerId'
