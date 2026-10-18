const mongodb = require("mongodb");
const url = "mongodb://localhost:5000/blogdb";
let g = null;

const main = async () => {
  const conn = await mongodb.MongoClient.connect(url);
  g = conn;
  return conn;
};

main();

module.exports = main;
