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
