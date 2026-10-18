const app = require('express')();
app.use(require('express').json());
app.get("/",(req, res) => console.log(req.headers?.authorization?.split(" ")[1]) || res.send("OK"));
app.listen(8080);
