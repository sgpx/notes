	
const serverless = require('serverless-http');
const express = require('express')
const app = express()

app.use(express.json());
 
app.get('/', function (req, res) {
  res.send('Hello World!')
})

app.post('/',(req,res) => {
	res.send('Hello POST!')
})
 
module.exports.handler = serverless(app);
