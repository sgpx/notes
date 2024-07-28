#!/bin/bash
aws ec2 describe-reserved-instances --query 'ReservedInstances[*].[ReservedInstancesId,InstanceType,AvailabilityZone,Start,End,InstanceCount]' --output table
