const mongoose = require("mongoose");

const CustomerSchema = mongoose.Schema({
	name : String,
	age : Number
});


const collectionName = "Customer456"; // will be lowercased in database
const Customer = mongoose.model(collectionName, CustomerSchema);

module.exports = Customer;
