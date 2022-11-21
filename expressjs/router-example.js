const express = require('express');

const router = express.Router();
router.get("/lol",(req, res) => res.send("OK"));

const app = express();
app.use(router);
app.listen(5000);
