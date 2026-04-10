import boto3
import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_bedrock_client():
    # Bedrock typically uses AWS credentials from environment/IAM roles
    # but we can check for a region as a proxy for configuration
    region = getenv("AWS_REGION", "eu-west-2")
    return boto3.client("bedrock-runtime", region_name=region)

def invoke(prompt, model="global.anthropic.claude-haiku-4-5-20251001-v1:0", temperature=0):
    client = get_bedrock_client()
    
    enhanced_prompt = (
        "Please follow instructions precisely and respond concisely without extra commentary.\n\n"
        + prompt
    )
    
    messages = [
        {"role": "user", "content": enhanced_prompt}
    ]
    
    return converse(messages=messages, model=model, temperature=temperature)

def converse(messages=[], model="global.anthropic.claude-haiku-4-5-20251001-v1:0", temperature=0):
    client = get_bedrock_client()
    
    # Payload structure for Anthropic Claude on Bedrock
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2048,
        "messages": messages,
        "temperature": temperature
    }
    
    response = client.invoke_model(
        modelId=model,
        body=json.dumps(payload)
    )
    
    response_body = json.loads(response.get("body").read())
    return response_body["content"][0]["text"]

def get_embedding(text: str, model="amazon.titan-embed-text-v1"):
    client = get_bedrock_client()
    
    payload = {
        "inputText": text
    }
    
    response = client.invoke_model(
        modelId=model,
        body=json.dumps(payload)
    )
    
    response_body = json.loads(response.get("body").read())
    # Titan returns 'embedding', Cohere returns 'embeddings'
    return response_body.get("embedding")