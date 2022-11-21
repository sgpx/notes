#!/usr/bin/env node

const express = require('express');
const app = express();
const port = process.env.PORT || 5000;

app.use(express.json());

app.get('/', (req, res) => {
  console.log(req);
  res.send('Hello World!');
});

app.post('/', (req, res) => {
  console.log(req);
  console.log(req.headers);
  console.log(req.body);
  res.send('Hello POST!');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})

