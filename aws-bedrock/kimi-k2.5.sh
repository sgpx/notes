#!/bin/bash
model="moonshot.kimi-k2.5-v1:0"
nano ~/prog/gpt4/a.txt
a=$(cat ~/prog/gpt4/a.txt)

# Updated JSON payload structure for Moonshot Kimi API requirements
json=$(jq -n --arg a "$a" '{"messages":[{"role":"user", "content":$a}], "max_tokens": 4096}')
printf "%s" "$json" > /tmp/z.out

fn="$HOME/prog/gpt4/kimi2.5-$(date +%s).txt"

# Invoking the model on us-east-1
AWS_DEFAULT_REGION=us-east-1 aws bedrock-runtime invoke-model --model-id "$model" --body "$(base64 -i /tmp/z.out)" "$fn"

# Updated parsing logic to match Moonshot's response format
jq -r ".choices[0].message.content" $fn
