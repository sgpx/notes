# AWS Simple Notification Service

# example

sending sms

```
#!/bin/bash
target_number=$1
otp=$2
aws sns set-sms-attributes --attributes '{"DefaultSenderID":"FOOBAR", "DefaultSMSType":"Transactional"}'
aws sns publish --phone-number $target_number --region ap-south-1 --message "Your OTP is $otp"
```
