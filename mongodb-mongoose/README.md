# mongoose

"Object Data Modeling (ODM) library for MongoDB and Node.js. It manages relationships between data, provides schema validation, and is used to translate between objects in code and the representation of those objects in MongoDB."

# connection

```
const mongoose = require("mongoose");
await mongoose.connect("mongodb://localhost:27017");
console.log(mongoose.connection);
```

# switch database (creates a new connection)

```
const mongoose = require("mongoose");
const conn = await mongoose.connect("mongodb://localhost:27017");
console.log(mongoose.connection);
const mydb = conn.useDb("mydb");
console.log(mydb.name);
```
# connection.useDb()



# links


https://www.freecodecamp.org/news/introduction-to-mongoose-for-mongodb-d2a7aa593c57/

https://mongoosejs.com/docs/api/connection.html#connection_Connection-useDb
