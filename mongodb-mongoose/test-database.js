const mongoose = require("mongoose");

const main = async () => {
  const conn = await mongoose.connect("mongodb://localhost:5000/tsdb");
  const mydb = mongoose.connection.useDb("mydb");
  // does not work

  const Customer = require("./models/Customer");
  await Customer.create({ name: "foobar", age: 123 });
  process.exit(0);
};

const main2 = async () => {
  await mongoose.connect("mongodb://localhost:5000/testdb");

  const conn = mongoose.connection;
  console.log(conn);
  console.log(conn.host);
  console.log(conn.port);

  console.log(conn.name);
  console.log(conn.db.namespace);

  const db2 = conn.useDb("exampledb");

  console.log(db2.name);
  console.log(db2.namespace);

  process.exit(0);
};

main();
