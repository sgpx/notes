#!/usr/bin/env node
import express, { Request, Response, NextFunction, Express } from "express";
import { Pool, PoolClient } from "pg";

interface RequestWithPgClient extends Request {
  pgClient?: PoolClient;
}

const app: Express = express();
const port: number = 3001;
const dbPort: number = 4001;

const pool: Pool = new Pool({
  user: "username",
  host: "localhost",
  database: "xdb",
  password: "password",
  port: dbPort,
});

app.use(async (req: RequestWithPgClient, _: Response, next: NextFunction) => {
  const client: PoolClient = await pool.connect();
  req.pgClient = client;
  next();
});

app.get("/test", async (req: RequestWithPgClient, res: Response) => {
  try {
    const result = await req?.pgClient?.query("SELECT NOW()");
    const rows = result?.rows;
    res.json(rows);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).send("Internal Server Error");
  }
});

app.use(async (req: RequestWithPgClient, __: Response, next: NextFunction) => {
  req?.pgClient?.release();
  next();
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
