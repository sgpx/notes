const main = async () => {
  const m = require("mongoose");
  const a = "mongodb://localhost:5000/testdb";

  await m.connect(a);

  const petSchema = m.Schema({ name: String });
  const pet = m.model("pet", petSchema);

  const petName = `foobar ${new Date().getTime()}`;
  console.log(petName);

  const res1 = await pet.create({ name: petName });
  console.log("create", res1);

  const res2 = await pet.findOne({ name: petName });

  // const res2 = await pet.findOne({});
  console.log("findOne", res2);
  process.exit(0);
};

main();
