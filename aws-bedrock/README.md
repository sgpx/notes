# setup

```
brew install python
pip3 install langchain boto3 awscli
aws configure set region us-east-1
```

# bedrock client

`client = boto3.client('bedrock')`

# bedrock runtime client

`client = boto3.client('bedrock-runtime')`


# input inference parameters

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html#model-parameters-jurassic2

# boto3 invoke model docs

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model.html

# mistral large

mistral is a text completion model, not a chat model

as such it will still need formatting in a manual Q-A format

```
Question:
Answer:
```

# view inference profiles

https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html

```
aws bedrock list-inference-profiles
```

substitute the `inferenceProfileId` in the `modelId` for bedrock scripts

```
"inferenceProfileArn": "arn:aws:bedrock:ap-south-1:${ACCOUNT_ID}:inference-profile/apac.anthropic.claude-3-5-sonnet-20240620-v1:0",
```
