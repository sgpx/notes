# square bracket assignment (assign keys by variable value)

```
> a = 5
5
> {a: a}
{ a: 5 }
> {[a]: a}
{ '5': 5 }
```

# global namespace

```
global.foo = 1;
console.log(require("./echo_global.foo_module.js")()); // gives 1
```

# syntax check script without running

`node --check a.js`

`node -c a.js`

# evaluate scripts (command mode)

`node --eval='console.log(1+2);'`

# manage developer dependencies

developer dependencies are not included in production builds

`npm i -D nodemon`

`yarn add --dev nodemon`

`yarn add nodemon -D`

`yarn install --production=[true|false]`

# macOS homebrew node version change

```
brew unlink --force node@17
brew install node@16
brew link node@16
```

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
