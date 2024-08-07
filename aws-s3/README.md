# IAM policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::mybucket/*",
                "arn:aws:s3:::mybucket"
            ]
        }
    ]
}
```

# restricted putobject policy

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
                "arn:aws:s3:::mybucket/*",
                "arn:aws:s3:::mybucket"
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
                "arn:aws:s3:::mybucket/*",
                "arn:aws:s3:::mybucket"
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

# read HTML files from a public

files go into download mode in a browser because the Content-Type is not set therefore the server passes binary/octet-stream as the MIME type of the downloaded link

use this to avoid

```
def copy_to_s3(file_path, s3_object_key):
    s3_client = boto3.client("s3")
    res = s3_client.upload_file(file_path, bucket_name, s3_object_key, ExtraArgs={"ContentType":"text/html"})
```

AWS CLI (probably) does this automatically
