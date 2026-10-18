#!/bin/bash
role_arn=$(cat ~/role-arn.txt)

mkdir tlf3
cp lambda_function.default.py tlf3/lambda_function.py
cd tlf3
echo pwd: $PWD

rm -v ~/a.zip
zip -r ~/a.zip .


echo aws lambda create-function --function-name testlambdafunction3 --zip-file fileb://$HOME/a.zip --role $role_arn --runtime python3.9 --architectures arm64 --handler lambda_function.lambda_handler --timeout 900
aws lambda create-function --function-name testlambdafunction3 --zip-file fileb://$HOME/a.zip --role $role_arn --runtime python3.9 --architectures arm64 --handler lambda_function.lambda_handler --timeout 900

cd ..
echo pwd: $PWD
rm -rfv tlf3
