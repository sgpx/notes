#!/bin/bash
name="frontend"

if [ "$1" != "" ]; then
	name="$1"
fi

yarn create vite $name --template react-ts
cd $name
yarn
yarn add --dev prettier

rm -v .eslintrc*
cp -v ~/prog/notes/vite/fix*.eslintrc.json .eslintrc.json

echo '#!/bin/bash
yarn vite --host localhost --port 3000' > run.sh
chmod +x run.sh

rm -rf src
mkdir src

echo 'import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);' > src/main.tsx

echo 'const App = () => <div>Hello World!</div>;
export default App;' > src/App.tsx

npx prettier -w src/main.tsx
npx prettier -w src/App.tsx

jq '.scripts.start = "./run.sh"' package.json > pkg2.json
mv -v pkg2.json package.json
