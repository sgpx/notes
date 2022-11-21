#!/usr/bin/env node

const pg = require("pg");
const express = require("express");
const app = express();
const port = process.env.PORT || 5000;
const db_url = process.env.DATABASE_URL;

app.use(express.json());

app.get("/", async (req, res) => {
  const pool = new pg.Pool({
    connectionString: db_url,
    ssl: { rejectUnauthorized: false },
  });
  pool.connect((err, client, releaseClient) => {
    if (err) {
      res.send(err.toString());
    } else {
      client
        .query("select * from test")
        .catch((err) => {
          res.status(500).send(err.toString());
        })
        .then((queryResponse) => {
          res.send(JSON.stringify(queryResponse.rows));
          releaseClient();
        });
    }
  });
});

app.post("/", (req, res) => {
  const rbody = req.body;

  const pool = new pg.Pool({
    connectionString: db_url,
    ssl: { rejectUnauthorized: false },
  });
  pool.connect((err, client, releaseClient) => {
    if (err) {
      res.send(err.toString());
    } else {
      client
        .query("insert into test(a,b) values($1,$2)", [rbody.a, rbody.b])
        .catch((err) => {
          res.status(500).send(err.toString());
        })
        .then((queryResponse) => {
          res.send(JSON.stringify(queryResponse));
          releaseClient();
        });
    }
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
