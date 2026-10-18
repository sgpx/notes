const main = async () => {

const m = require("mongoose");
const a = "mongodb://localhost:5000/testdb";

await m.connect(a);

const BlogPost = require("./models/BlogPost");



process.exit(0);

};

main();
