#!/usr/bin/env npx ts-node
import app from "./app";
const hostname: string = "localhost";
const port: number = 5000;

app.listen(port, hostname, () =>
  console.log(`listening on ${hostname}:${port}`)
);
