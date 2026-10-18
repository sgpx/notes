#!/usr/bin/env python3
import boto3
import json
import time

client = boto3.client("bedrock-runtime")
model_id = "amazon.nova-pro-v1:0"
print("enter prompt")
input_text_raw = input(">>> ")

model_response = client.converse(
    messages=[{"role": "user", "content": [{"text": input_text_raw.strip()} ]}], modelId=model_id
)

raw_response = model_response["output"]["message"]["content"][0]["text"]

print(raw_response)
ts = int(time.time())
fn = f"tg1-{ts}.json"
open(fn, "w").write(raw_response)
print("written to", fn)
