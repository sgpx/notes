#!/bin/bash
cd ~/prog/gpt4/
if [ "$1" = "--wipe" ]; then
	rm a.txt
fi
nano ~/prog/gpt4/a.txt

a=$(cat ~/prog/gpt4/a.txt)
json="{\"prompt\": \"$a\", \"maxTokens\": 8191}"
echo $json > /tmp/z.out
body=$(base64 -i /tmp/z.out)
fn="$HOME/prog/gpt4/j2u-$(date +%s).txt"
AWS_DEFAULT_REGION=us-east-1 aws bedrock-runtime invoke-model --model-id ai21.j2-ultra --body "$body" $fn
#jq '.' $fn
jq -r '.completions.[0].data.text' $fn
