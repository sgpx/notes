# typescript

# setup

```
yarn init --yes
yarn add ts-node typescript tslib @types/node
yarn run ts-node --eval 'console.log("123");'
```

# run scripts

`npx ts-node a.ts`

# compile to javascript

`npx tsc a.ts`
`npx tsc a.ts && node a.js`
`npx tsc a.ts --target esnext && node a.js`
`yarn run tsc a.ts --target es5 && node a.js`
