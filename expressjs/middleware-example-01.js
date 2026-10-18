const express = require("express");

const app = express();
app.use(express.json());

const myMiddleWare = (req, res, next) => {
  console.log(req.method);
  if (req.method === "POST") {
    console.log(req.headers);
    console.log(req.body);

    if (req.body.a !== "1") return res.status(401).send("ERROR");
    next();
  } else {
    next();
  }
};

const middleWareTwo = (req, res, next) => {
	console.log("middleWareTwo");
	next();
}

app.use(myMiddleWare);

//using middleware on a specific route
app.use("/mw2", middleWareTwo);

app.get("/mw2", (req, res) => res.send("mw2 OK"));

app.get("/", (req, res) => res.send("OK"));
app.post("/", (req, res) => res.send("OK"));

app.listen(4000, () => console.log("listening on port 4000"));
