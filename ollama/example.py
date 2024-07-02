#!/usr/bin/env python3
import requests as r
import json, sys

url = "http://localhost:11434/api/chat"
rj = {"model":"phi3","messages":[{"role":"system","content":"you are the manager of a software consulting company with 1 engineer. you have to supervise the work of the engineer and outline tasks for him."},{"role":"user","content":"i need to create a pytorch machine learning model for client 1 and a ETL pipeline for client 2"}],"options":{"temperature":0},"stream":True}

resp = r.post(url, json=rj, stream=True)

for line in resp.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line).get("message").get("content"), end="")
        sys.stdout.flush()
