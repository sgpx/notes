# install

`yarn add mathjax-node`

# usage

```javascript
const mathjax = require("mathjax-node");
await mathjax.start();
const latex = "$$ P(X=1/k) = f(x_n) $$";
const mml = (await mathjax.typeset({ math: latex, format: "TeX", mml: true }))?.mml
console.log(mml);
```
