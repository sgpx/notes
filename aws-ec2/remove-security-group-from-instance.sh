#!/bin/bash
echo "===="
bash get-instance-vpcs.sh
echo "===="
bash get-all-security-groups.sh
echo "===="
echo enter instance id
read instance_id
echo "===="
bash instance-get-security-groups.sh $instance_id
echo "===="
echo enter group to be deleted
read target_group


newgroups=$(bash instance-get-security-groups.sh $instance_id | sed -r "s/$target_group//g")

aws ec2 modify-instance-attribute --instance-id $instance_id --groups $newgroups

echo deleted $target_group

bash instance-get-security-groups.sh $instance_id

bash delete-unused-security-groups.sh
