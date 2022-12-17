const express = require('express');
const app = express();
app.use(express.json());


app.use("/api/:path", (req, res, next) => {
	console.log(req.baseUrl);
	return res.send("OK");
})

app.get("/", (req,res) => res.send("ok"));

app.listen(3000);
