#!/bin/bash
aws lambda update-function-code --function-name myfunc --zip-file fileb://a.zip
