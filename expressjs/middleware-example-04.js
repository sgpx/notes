const express = require("express");
const app = express();
app.get("/api/xyz", (req, res) => res.send("OK1"));
app.use("/api/:path", (req, res, next) => {
        console.log("OK2");
        next();
});

app.use("/api2/:path", (req, res, next) => {
        console.log("OK2");
        next();
});
app.get("/api2/xyz", (req, res) => res.send("OK1"));


app.listen(3000);
