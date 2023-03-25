const a = require("express");
const app = a();
const b = require("next");
const c = b({ __dirname: "." });

c.prepare().then(() => {
  const handler = c.getRequestHandler();
  app.use("/", (req, res) => handler(req, res));
  app.use("/", async (req, res) => {
    console.log(req.path, req.url);
    const d = c.render(req, res, req.path, req.query);
    console.log(await d);
    return d;
  });
  app.listen(3005, () => console.log("123"));
});
