# SNS



# dynamodb

## create a client object

```javascript
#!/usr/bin/env node

const credentials = require('./env.js');

const { DynamoDBClient } = require('@aws-sdk/client-dynamodb')

const client =  new DynamoDBClient({region: "ap-south-1", credentials: credentials});

```

## send a command through the client

```javascript

const { ListTablesCommand } = require('@aws-sdk/client-dynamodb');

const command = new ListTablesCommand({});

client.send(command).then(console.log);

```

## list tables command

```javascript

const { ListTablesCommand } = require('@aws-sdk/client-dynamodb');

const command = new ListTablesCommand({});

client.send(command).then(console.log);

```

## describe table command

```javascript

const { DescribeTableCommand } = require('@aws-sdk/client-dynamodb');

const command = new DescribeTableCommand({ TableName : "test_db" });

client.send(command).then(console.log);

```
