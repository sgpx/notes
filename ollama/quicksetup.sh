#!/bin/bash
sudo snap install docker
sudo docker pull ollama/ollama
sudo docker run --name o1 -it -d -p 11434:11434 ollama/ollama
sudo docker exec o1 ollama pull phi3:mini
#sudo docker exec o1 ollama serve
