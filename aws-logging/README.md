# logs

## get log group names

`aws logs describe-log-groups`

## get log streams for a log group

`aws logs describe-log-streams --log-group-name /aws/lambda/foo-lambda-app`

## get log events from a log stream

`aws logs get-log-events --log-group-name /aws/lambda/foo-lambda-app --log-stream-name 2021/12/12/[\$LATEST]xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
