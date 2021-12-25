# cloudformation cli

## stack

A stack is a collection of AWS resources that you can manage as a single unit

## list stacks

`aws cloudformation list-stacks`

## get list of resources in stack

`aws cloudformation describe-stack-resources --stack-name my-stack-name`

## get a particular resource

`aws cloudformation describe-stack-resource  --stack-name lambda-stack-one --logical-resource-id IamRoleLambdaExecution`

`aws cloudformation describe-stack-resource  --stack-name lambda-stack-one --logical-resource-id AppLogGroup`
