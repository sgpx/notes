const port = process.env.BACKEND_PORT;
const dbUrl = process.env.DATABASE_URL;
const { Pool } = require("pg");
const express = require("express");
const cors = require("cors");
const app = express();

const pool = new Pool({ connectionString: dbUrl });

app.use(cors());
app.use(express.json());

app.get("/", async (_, res) => {
  const pgClient = await pool.connect();
  try {
    await pgClient.query(
      "insert into recipes(date_created_at, recipe_topic) values($1, $2);",
      [new Date().toISOString(), "something"]
    );

    const result = await pgClient.query("select * from recipes;");
    res.json({ r: result.rows[0] });
  } catch (error) {
    console.error(error);
    res.sendStatus(500);
  } finally {
    pgClient.release();
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
