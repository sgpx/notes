# installing

`yarn add aws-sdk`

# setup credentials

```

import AWS from 'aws-sdk';
// for nodejs/commonjs
// const AWS = require('aws-sdk');

AWS.config.update({
   region: "ap-south-1",
   credentials: {secretAccessKey: "...", accessKeyId: "..."},
});

```

## dynamodb client

```
const DynamoDBClient = new AWS.DynamoDB();
```

### list tables

```
DynamoDBClient.listTables(console.log)
```

### create table

```
const params = params = {
    TableName : "test_db",
    KeySchema: [       
        { AttributeName: "year", KeyType: "HASH"},  //Partition key
        { AttributeName: "title", KeyType: "RANGE" }  //Sort key
    ],
    AttributeDefinitions: [       
        { AttributeName: "year", AttributeType: "N" },
        { AttributeName: "title", AttributeType: "S" }
    ],
    ProvisionedThroughput: {       
        ReadCapacityUnits: 10, 
        WriteCapacityUnits: 10
    }
};
DynamoDBClient.createTable(params,console.log)
```

### delete table

```
DynamoDBClient.deleteTable({TableName: "test_db"},console.log)
```

### scan limits

```javascript

let lastEvaluatedKey = null;
DynamoDBClient.scan({TableName: "test_db"}, (err, data) => {
	lastEvaluatedKey = data.LastEvaluatedKey;
	console.log(data);
});

while(lastEvaluatedKey)
{
	DynamoDBClient.scan({TableName: "test_db", ExclusiveStartKey: lastEvaluatedKey}, (err, data) => {
		lastEvaluatedKey = data.LastEvaluatedKey ? data.LastEvaluatedKey : null;
		console.log(data);
	});
}

```
