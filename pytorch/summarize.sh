#!/bin/bash
LLM=qwen25.sh
function fxn() {
	stat -f "%SB" $1
}

if [ $(pgrep -f -i ollama) ]; then ollama serve & fi

echo "filename,description,creation_date"
for curr_file in $(ls *.py); do printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $curr_file >> ~/prog/gpt4/a.txt ; echo $(basename $PWD)/${curr_file},$($LLM --noconfirm),$(fxn $curr_file) ; done
if [ $(pgrep -f -i ollama) ! = "" ]; then kill -9 $(pgrep -f -i ollama) ; fi
