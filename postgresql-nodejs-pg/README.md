# setup

`yarn add pg`

# client connection pooling (avoid `client is already connected` errors)

https://en.wikipedia.org/wiki/Connection_pool

```
app.get("/", async (req, res) => {
  const pool = new pg.Pool({
    connectionString: db_url,
    ssl: { rejectUnauthorized: false },
  });
  pool.connect((err, client, releaseClient) => {
    if (err) {
      res.send(err.toString());
    } else {
      client.query("select * from test").then((queryResponse) => {
        res.send(JSON.stringify(queryResponse.rows));
        releaseClient(); // release client back into the pool
      });
    }
  });
});
```
