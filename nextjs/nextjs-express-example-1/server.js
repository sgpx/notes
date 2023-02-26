const express = require("express");
const next = require("next");

const app = next({ dev: true, __dirname : "." });
console.log(app);
app.prepare().then(() => {
  console.log("prepare OK");
  const mainServ = express();
  mainServ.use(
    "/",
    (req, res) => console.log(`got url ${req.url}`) || app.render(req, res, req.path, req.query)
  );
  mainServ.listen(8080, () => console.log("listening"));
});
