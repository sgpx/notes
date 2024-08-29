#!/bin/bash
if [ "$1" = "--wipe" ]; then
	rm ~/prog/gpt4/a.txt
fi
model_id="meta.llama3-1-70b-instruct-v1:0"

nano ~/prog/gpt4/a.txt
a=$(cat ~/prog/gpt4/a.txt)
json=$(jq -n --arg prompt "$a" --argjson max_gen_len 2048 '{prompt: $prompt, max_gen_len: $max_gen_len}')
echo $json > /tmp/z.out
fn="$HOME/prog/gpt4/mistral-$(date +%s).txt"
AWS_DEFAULT_REGION=us-west-2 aws bedrock-runtime invoke-model --model-id $model_id --body "$(base64 -i /tmp/z.out)" $fn
cat $fn
