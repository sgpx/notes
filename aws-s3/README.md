# restricted put policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::lplt-static/*",
                "arn:aws:s3:::lplt-static"
            ]
        },
        {
            "Sid": "Statement2",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::1234567890:user/my-iam-user",
            },
            "Action": "s3:PutObject",
            "Resource": [
                "arn:aws:s3:::lplt-static/*",
                "arn:aws:s3:::lplt-static"
            ]
        }
    ]
}
```

# make bucket objects publicly accessible

https://medium.com/@chandrapal/bucket-policy-for-your-public-s3-bucket-7549c7e50acd

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1405592139000",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::bucketname/*",
                "arn:aws:s3:::bucketname"
            ]
        }
    ]
}
```

# SDK reference


https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getObject-property

https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#putObject-property

https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#listObjects-property
