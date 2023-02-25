#!/bin/bash
a=$(aws cloudformation describe-stacks --region ap-south-1 | jq -r '.Stacks | map (.StackId) | .[]')
for i in $a; do 
	echo deleting $i..; 
	echo aws cloudformation delete-stack --stack-name $i; 
	aws cloudformation delete-stack --stack-name $i; 
done
