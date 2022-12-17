const express = require('express');
const app = express();
app.use(express.json());


app.use((req, res, next) => {
	console.log(req.url);
	next();
})

app.get("/", (req,res) => res.send("ok"));

app.listen(3000);
