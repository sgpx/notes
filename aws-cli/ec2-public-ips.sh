#!/bin/bash
aws ec2 describe-instances --region $1 | jq '.Reservations | map (.Instances) | .[] | map (.PublicIpAddress)'
