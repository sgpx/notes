#!/bin/bash
name="frontend"
engine="pnpm"
install_verb="add"
exec_engine="pnpm"

if [[ "$1" != "" && "$1" != "--tailwind" ]]; then
    name="$1"
fi

$engine create vite $name --template react-ts
cd $name
$engine install

# Install dev dependencies
$engine $install_verb -D prettier

# Set up ESLint config if available
rm -v .eslintrc* 2>/dev/null || true
cp -v ~/prog/notes/vite/fix*.eslintrc.json .eslintrc.json 2>/dev/null || true

# Create run script
echo '#!/bin/bash
'"$engine"' vite --host localhost --port 3000' > run.sh
chmod +x run.sh

# Set up src directory
rm -rf src
mkdir src

if [[ "$1" = "--tailwind" || "$2" = "--tailwind" ]]; then
    echo 'import "./index.css";' > src/main.tsx
else
    echo '' > src/main.tsx
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

# Format files with prettier
$engine exec prettier -w src/main.tsx
$engine exec prettier -w src/App.tsx

# Update package.json
jq '.scripts.start = "./run.sh"' package.json > pkg2.json
mv -v pkg2.json package.json

# Set up Tailwind if requested
if [[ "$1" = "--tailwind" || "$2" = "--tailwind" ]]; then
    # Install Tailwind with the new Vite plugin approach
    $engine $install_verb -D tailwindcss @tailwindcss/vite postcss autoprefixer
    
    # Create a basic tailwind.config.js
    echo "/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}" > tailwind.config.js
    
    # Create index.css with Tailwind directives
    echo '@import "tailwindcss";' > src/index.css
    
    # Update vite.config.ts to use the Tailwind plugin
    echo "import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
})" > vite.config.ts
    
    # Create a global.d.ts file
    echo '/// <reference types="vite/client" />' > src/global.d.ts
    
    # Update App.tsx with a Tailwind example
    echo 'const App = () => (
  <div className="min-h-screen bg-gray-100 flex items-center justify-center">
    <div className="bg-white p-8 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">
        Hello Tailwind CSS!
      </h1>
      <p className="text-gray-600">
        This project is set up with Vite, React, TypeScript, and Tailwind CSS.
      </p>
    </div>
  </div>
);

export default App;' > src/App.tsx
    
    # Format the updated App file
    $engine exec prettier -w src/App.tsx
fi

echo "Setup complete! Run 'cd $name && $engine start' to start the development server."