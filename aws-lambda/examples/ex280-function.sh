#!/bin/bash
role_arn="arn:..."
FUNC_NAME="..."
S3_BUCKET="mybucket"
S3_KEY="${FUNC_NAME}.zip"

rm -v ~/a.zip
cp lambda.zip ~/a.zip

aws s3 cp "$HOME/a.zip" "s3://$S3_BUCKET/$S3_KEY"

if [ "$1" != "--create" ] ; then
	aws lambda update-function-code --function-name "$FUNC_NAME" --s3-bucket "$S3_BUCKET" --s3-key "$S3_KEY" --architectures arm64
	aws s3 rm "s3://$S3_BUCKET/$S3_KEY"
	exit 0
fi



echo aws lambda create-function --function-name "$FUNC_NAME" --code "S3Bucket=$S3_BUCKET,S3Key=$S3_KEY" --role "$role_arn" --runtime python3.12 --architectures arm64 --handler lambda_function.lambda_handler --timeout 900
aws lambda create-function --function-name "$FUNC_NAME" --code "S3Bucket=$S3_BUCKET,S3Key=$S3_KEY" --role "$role_arn" --runtime python3.12 --architectures arm64 --handler lambda_function.lambda_handler --timeout 900
