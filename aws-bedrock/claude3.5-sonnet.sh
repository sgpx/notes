#!/bin/bash
#model="anthropic.claude-3-sonnet-20240229-v1:0"
model="anthropic.claude-3-5-sonnet-20240620-v1:0"
if [ "$1" = "--wipe" ]; then
	rm ~/prog/gpt4/a.txt
fi

if [ "$1" != "--noconfirm" ]; then
	nano ~/prog/gpt4/a.txt
fi

a=$(cat ~/prog/gpt4/a.txt)
json=$(jq -n --arg a "$a" '{"messages":[{"role":"user", "content":$a}], "max_tokens": 4096, "anthropic_version": "bedrock-2023-05-31"}')
printf "%s" "$json" > /tmp/z.out
fn="$HOME/prog/gpt4/claude-$(date +%s).txt"
AWS_DEFAULT_REGION=us-east-1 1>/dev/null aws bedrock-runtime invoke-model --model-id "$model" --body "$(base64 -i /tmp/z.out)" "$fn"
jq -r ".content[0].text" $fn
