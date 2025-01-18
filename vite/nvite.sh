#!/bin/bash
name="frontend"

if [[ "$1" != "" && "$1" != "--tailwind" ]]; then
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


if [ "$1" = "--tailwind" ]; then
	echo 'import "./index.css";' > src/main.tsx
fi

echo 'import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);' >> src/main.tsx

echo 'const App = () => <div>Hello World!</div>;
export default App;' > src/App.tsx

npx prettier -w src/main.tsx
npx prettier -w src/App.tsx

jq '.scripts.start = "./run.sh"' package.json > pkg2.json
mv -v pkg2.json package.json

if [ "$1" = "--tailwind" ]; then
	yarn add --dev tailwindcss postcss autoprefixer
	yarn tailwindcss init -p
	cp -v ~/prog/notes/vite/tailwind-files/tailwind.config.js .	
	cp -v ~/prog/notes/vite/tailwind-files/index.css src/index.css
	cp -v ~/prog/notes/vite/tailwind-files/global.d.ts src/global.d.ts
fi
