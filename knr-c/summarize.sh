#!/bin/bash
LLM=qwen25.sh

function get_date_string() {
        stat -f "%SB" $1
}

if [ "$(pgrep -f -i ollama)" ]; then ollama serve & fi
for i in $(find . -type f -iname "*.c" | sort -n); do 
	a=$(grep "$i" ~/prog/mluniv/knr-c.md)
	if [ "$1" = "-s" ]; then
		if [ "$a" != "" ]; then 
			echo skipping $i ; 
			continue ; 
		else
			printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo "$(basename $PWD)/${i},$($LLM --noconfirm),$(get_date_string $curr_file)" >> ~/prog/mluniv/knr-c.md ; 
		fi
	else
			printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo "$(basename $PWD)/${i},$($LLM --noconfirm),$(get_date_string $curr_file)" ; 

	fi
done

if [ "$(pgrep -f -i ollama)" != "" ]; then kill -9 $(pgrep -f -i ollama) ; fi
