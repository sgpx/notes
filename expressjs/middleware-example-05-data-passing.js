const app = require("express")();
app.use("/", (req, res, next) => {
        req.xdata = {a : "b"};
        return next();
});
app.get("/", (req, res) => console.log(req) || res.json(req.xdata));
app.listen(3000);
