#!/usr/bin/env python3
import boto3
import json
import time

client = boto3.client("bedrock-runtime")
model_id = "meta.llama2-70b-chat-v1"
print("enter prompt")
input_text_raw = input(">>> ").strip()
prompt_body = json.dumps({"prompt": input_text_raw, "max_gen_len": 2048})
invocation_response = client.invoke_model(
    body=prompt_body.encode("utf-8"), modelId=model_id
)

raw_response = invocation_response["body"].read().decode("utf-8")
response_data = json.loads(raw_response)
print(response_data.get("generation"))
fn = f"llama2-70b-{int(time.time())}.json"
open(fn,"w").write(raw_response)

print(f"\n\nwritten to {fn}")
