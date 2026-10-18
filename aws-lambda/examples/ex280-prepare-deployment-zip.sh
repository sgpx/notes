#!/bin/bash
a=$(podman machine inspect | jq -r '.[0].State') 
echo $a
if [ "$a" != "running" ]; then
	podman machine start
fi
stop-docker-containers.sh --rm
podman run --name a1 -it -d ubuntu:24.04 bash
podman exec -it a1 /bin/bash -lc "nohup apt update && nohup apt install -y python3 python3-pip && mkdir /root/lambda && cd /root/lambda && pip install -t . openai python-dotenv onnxruntime numpy"
podman cp .env a1:/root/lambda/
podman cp ../ex280.onnx a1:/root/lambda/
podman cp ../ex280.onnx.data a1:/root/lambda/
podman cp llm.py a1:/root/lambda/
podman cp lambda_function.py a1:/root/lambda/
podman exec -it a1 /bin/bash -lc "cd /root/lambda && zip -r /root/a.zip ."
podman cp a1:/root/a.zip lambda.zip
