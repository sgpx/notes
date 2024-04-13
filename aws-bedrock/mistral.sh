#!/bin/bash
nano ~/prog/gpt4/a.txt
a=$(cat ~/prog/gpt4/a.txt)
json="{\"prompt\": \"$a\", \"max_tokens\": 4096}"
echo $json > /tmp/z.out
fn="$HOME/prog/gpt4/mistral-$(date +%s).txt"
AWS_DEFAULT_REGION=us-east-1 aws bedrock-runtime invoke-model --model-id mistral.mixtral-8x7b-instruct-v0:1 --body "$(base64 -i /tmp/z.out)" $fn
jq -r '.outputs[0].text' $fn
