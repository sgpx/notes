# JWT - json web tokens

## nodejs setup

see `nodejs-example/`

```js

#!/usr/bin/env node

const jwt = require('jsonwebtoken');
console.log(jwt);

const secret = "123";

const payload = { iat: new Date().getTime(), exp: new Date().getTime() + 1000, data: "blah" };

const token = jwt.sign(payload, secret, {algorithm: "HS256"});

console.log(token);

```
