# next.js

server side rendering for react

# quick start

```
mkdir pages
echo "const Index = () => <div>hello world</div>;" >> pages/index.js
echo "export default Index;" >> pages/index.js
yarn init --yes
yarn add react react-dom next
yarn next
```

# create app

`yarn create next-app my-nextjs-app`

`npx create-next-app`


# export app and serve static

```
yarn add serve
yarn next build
yarn next export
yarn serve -s out/
```

# start dev server on ip address

```
yarn next build
yarn next dev --hostname 192.168.0.1 --port 3000
```

# serve build on ip address

```
yarn next build
yarn next start -H 192.168.0.1 -p 3000
```
