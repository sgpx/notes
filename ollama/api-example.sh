#!/bin/bash
curl -v http://localhost:11434/api/chat -d '{"model":"llama3","messages":[{"role":"system","content":"you are the manager of a software consulting company with 1 engineer. you have to supervise the work of the engineer and outline tasks for him."},
{"role":"user","content":"i need to create a pytorch machine learning model for client 1 and a ETL pipeline for client 2"}],"options":{"temperature":0},"stream":false}'
