#!/bin/bash
if [ $(pgrep -f -i ollama) ]; then ollama serve & fi
for i in $(ls *.py); do printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo $(basename $PWD)/${i},$(qwen25.sh --noconfirm) ; done
kill -9 $(pgrep -f -i ollama)
