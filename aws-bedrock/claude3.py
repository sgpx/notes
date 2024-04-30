import boto3
import json


def invoke(prompt):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    prompt_body = json.dumps(
        {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4096,
            "anthropic_version": "bedrock-2023-05-31",
        }
    )
    invocation_response = client.invoke_model(
        body=prompt_body.encode("utf-8"), modelId=model_id
    )
    raw_response = invocation_response["body"].read().decode("utf-8")
    response_data = json.loads(raw_response)
    ret = response_data.get("content")[0].get("text")
    return ret

if __name__ == "__main__":
    print(invoke(prompt="what is the type of algorithm is ARIMA?"))
