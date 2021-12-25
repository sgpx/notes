# exporting commonJS modules

myModule.js

```
const myObject = { a : 1, b : 2 };
module.exports = myObject;
```

index.js

```javascript
const myModule = require('./myModule.js');
console.log(myModule);
```
