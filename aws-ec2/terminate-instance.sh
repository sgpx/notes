#!/bin/bash
cd ~/prog/notes/aws-ec2
bash get-instance-ips.sh
echo enter instance id
read inst
aws ec2 modify-instance-attribute --instance-id $inst --attribute disableApiTermination --value False
aws ec2 terminate-instances --instance-ids $inst
