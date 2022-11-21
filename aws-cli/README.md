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
