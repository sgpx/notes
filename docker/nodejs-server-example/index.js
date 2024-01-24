const app = require('express')();
const cors = require('cors');
app.use(cors());

app.use((req,res,next) => {
	console.log("log:", req.ip, req.method, req.url);
	next();
});

app.get("/", (req, res) => res.send("hello from docker"));
app.listen(3000);
