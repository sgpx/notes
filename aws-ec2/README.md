# aws cli

## setup

```bash
sudo pip3 install awscli
aws configure
```

### set region programatically

aws configure set default.region us-east-1

### get spot instance public ip address

```
#!/bin/bash
aws ec2 describe-instances | jq '.Reservations[0].Instances[0].NetworkInterfaces[0].PrivateIpAddresses[0].Association.PublicIp'
```

# stop instance

```
aws ec2 stop-instances --instance-ids i-0123123123213
aws ec2 stop-instances --instance-ids i-0123123123213 --force # force stop
```

# describe instances


```
aws ec2 describe-instances
aws ec2 describe-instances --instance-ids i-0123123123213
```

# get instance state

```
ws ec2 describe-instances --instance-id i-0123123123123 | jq '.Reservations[0].Instances[0].State'
```

# delete security group

```
aws ec2 delete-security-group --group-id sg-XXXXXXX
```

# get all security groups for each instance


```
aws ec2 describe-instances | jq -r '.Reservations[].Instances[] | .InstanceId + " # "  + .SecurityGroups.[].GroupId + " # " + (.Tags.[] | .Value)'
```

# get security group of an instance

```
aws ec2 describe-instances --instance-id i-XXXXXX | jq '.Reservations[].Instances[].SecurityGroups'
```

# query syntax

```
aws ec2 describe-instances --query "Reservations[*].Instances[*].{Id: InstanceId, Name: Tags[0].Value, IP: PublicIpAddress}"
```

# add tags to instance

`aws ec2 create-tags --resources i-0b0123123123123 --tags "Key='Name',Value='slamtest2'"`
