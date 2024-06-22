#!/bin/bash
aws lambda update-function-code --function-name myfunc --zip-file fileb://a.zip

aws lambda invoke --function-name myfunc outfile.txt 

cat outfile.txt


