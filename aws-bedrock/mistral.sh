#!/bin/bash
if [ "$1" = "--wipe" ]; then
	rm ~/prog/gpt4/a.txt
fi
#model_id="mistral.mixtral-8x7b-instruct-v0:2"
model_id="mistral.mistral-large-2407-v1:0"

nano ~/prog/gpt4/a.txt
a=$(cat ~/prog/gpt4/a.txt)
#json="{\"prompt\": \"$a\", \"max_tokens\": 8192}"
json=$(jq -n --arg prompt "$a" --argjson max_tokens 8192 '{prompt: $prompt, max_tokens: $max_tokens}')
echo $json > /tmp/z.out
fn="$HOME/prog/gpt4/mistral-$(date +%s).txt"
AWS_DEFAULT_REGION=us-west-2 aws bedrock-runtime invoke-model --model-id $model_id --body "$(base64 -i /tmp/z.out)" $fn
jq -r '.outputs[0].text' $fn
