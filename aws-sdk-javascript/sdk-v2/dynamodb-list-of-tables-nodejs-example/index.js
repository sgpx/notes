const credentials = require('./env.js');
const aws = require('aws-sdk');

aws.config.update({ region : "ap-south-1", credentials : credentials })

const db = new aws.DynamoDB();

db.listTables(console.log);
