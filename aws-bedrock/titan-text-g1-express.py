#!/usr/bin/env python3
import boto3
import json
import time

client = boto3.client("bedrock-runtime")
model_id = "amazon.titan-text-express-v1"
print("enter prompt")
input_text_raw = input(">>> ")
prompt_body = json.dumps({
    "inputText": input_text_raw.strip(),
    "textGenerationConfig": {"maxTokenCount": 4096},
})

invocation_response = client.invoke_model(body=prompt_body.encode("utf-8"), modelId=model_id)

raw_response = invocation_response["body"].read().decode("utf-8")
response_data = json.loads(raw_response)
for i in response_data.get("results"):
	print(i.get("outputText"))

ts = int(time.time())
fn = f"tg1-{ts}.json"
open(fn,"w").write(raw_response)
print("written to", fn)
