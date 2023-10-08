#!/usr/bin/env python3
import boto3
import json
import time

client = boto3.client("bedrock-runtime")
model_id = "ai21.j2-ultra-v1"
print("enter prompt")
input_text_raw = input(">>> ")
input_dict = {"prompt": input_text_raw, "maxTokens": 8191}
prompt_body = json.dumps(input_dict)

j2 = client.invoke_model(body=prompt_body.encode("utf-8"), modelId=model_id)

raw_response = j2["body"].read().decode("utf-8")
response_data = json.loads(raw_response)
response_completions = response_data["completions"]

for i in response_completions:
    print(i.get("data", {}).get("text"))

ctime = int(time.time())
fn = f"j2-resp-{ctime}.txt"

open(fn, "w").write(raw_response)
print("wrote to", fn)
