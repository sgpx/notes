import boto3
import json
from botocore.exceptions import ClientError

def invoke_lambda(input_body: str) -> dict:
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='myfunc',
        Payload=json.dumps({"body": input_body})
    )
    
    response_payload = response['Payload'].read().decode('utf-8')
    return json.loads(response_payload)
