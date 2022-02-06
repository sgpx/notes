#!/bin/bash
git clone https://github.com/swagger-api/swagger-editor sw
cd sw
npm i 
npm run build
podman build -t swagger-editor-aarch64 .
podman run -d -p 8080:8080 swagger-editor-aarch64 
echo running on 8080
podman ps -a
