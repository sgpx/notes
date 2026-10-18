const serverless = require("serverless-http");
const express = require("express");
const app = express();
const nextjs = require("next");
const nextApp = nextjs({ dev: false, __dirname: "." });
app.get("/", async (req, res, next) => {
  await nextApp.prepare();
  return nextApp.render(req, res, "/", req.query);
});

app.use((req, res, next) => {
  return res.status(404).json({
    error: "Not Found",
  });
});

module.exports.handler = serverless(app);
