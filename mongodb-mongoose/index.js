const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:5000/exampledb");

const Customer = require("./models/Customer");

const next = (e) => {
  console.log(e);
  process.exit(0);
};

const getNumber = () => {
	return parseInt(Math.random() * 1000);
}

Customer.create({ name: `foo ${getNumber()}`, age: getNumber() }).then(next).catch(next);
