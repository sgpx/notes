# pass on middleware data to request

```
app.use("/", (req, res, next) => {
        req.xdata = {a : "b"};
        return next();
});
app.get("/", (req, res) => console.log(req) || res.json(req.xdata));
app.listen(3000);
```

# express header handling

`req.headers?.authorization`

# express.json() middleware

always add `Content-Type: application/json` header to request to get actual data

# middleware sequence matters

```
const express = require("express");
const app = express();
app.get("/api/xyz", (req, res) => res.send("OK1"));
app.use("/api/:path", (req, res, next) => {
	console.log("OK2");
	next();
});
app.listen(3000);
```


```
app.get("/api/", (_, res) => res.send("OK"));
app.use(expressStatic("public"));
```
