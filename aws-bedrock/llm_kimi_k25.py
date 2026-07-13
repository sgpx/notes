from typing import Any, Dict, List
import boto3
from botocore.exceptions import ClientError

# Global constants for the module
DEFAULT_MODEL = "moonshotai.kimi-k2.5"
DEFAULT_REGION = "us-east-1"


def invoke(
    prompt: str, model: str = DEFAULT_MODEL, region_name: str = DEFAULT_REGION
) -> str:
    """Sends a single text string prompt to the model and returns the text response."""
    messages = [{"role": "user", "content": [{"text": prompt}]}]
    return converse(messages, model_id=DEFAULT_MODEL, region_name=region_name)


def converse(
    messages: List[Dict[str, Any]],
    model: str = DEFAULT_MODEL,
    region_name: str = DEFAULT_REGION,
    reasoning_effort="high",
) -> str:
    """Sends a structured message list to the AWS Bedrock Converse API."""
    if reasoning_effort not in ["medium", "high"]:
        reasoning_effort = "medium"
    client = boto3.client("bedrock-runtime", region_name=region_name)

    try:
        print(model)
        messages = [
            {"role": j.get("role"), "content": [{"text": j.get("content")}]}
            for j in messages
        ]
        response = client.converse(
            modelId=DEFAULT_MODEL,
            messages=messages,
            additionalModelRequestFields={"reasoning_config": reasoning_effort},
        )
        return response["output"]["message"]["content"][0]["text"]

    except ClientError as e:
        raise RuntimeError(f"AWS Bedrock API Call Failed: {e}")
