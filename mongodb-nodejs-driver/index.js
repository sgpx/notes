const mongodb = require("mongodb");
const url = "mongodb://localhost:5000/testdb";
let g = null; 

const main = async () => {

const conn = await mongodb.MongoClient.connect(url);
g = conn;
console.log(conn);

const db = conn.db("testdb");

console.log(await db.collections());

await db.createCollection("xyz");

console.log(await db.collections());

console.log("deleting xyz");

await db.dropCollection("xyz");

console.log(await db.collections());

process.exit(0);
}

main();
