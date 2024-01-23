import express from "express";
import cors from "cors";
import ServerlessHttp from "serverless-http";

const app = express();
app.use(cors());

app.get("/", (req, res) => {
  console.log(req.path, req.method);
  res.json({ text: "OK" });
});

app.get("/test", (_, res) => res.send("test OK"));

export const handler = ServerlessHttp(app);