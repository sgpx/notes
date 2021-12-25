#!/usr/bin/env node

const credentials = require('./env.js');

const { DynamoDBClient, ListTablesCommand } = require('@aws-sdk/client-dynamodb')

const client =  new DynamoDBClient({region: "ap-south-1", credentials: credentials});

const command = new ListTablesCommand({});

client.send(command).then(console.log, console.log);
