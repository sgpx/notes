#!/bin/bash
llm_exec="node index.js"
target_file=~/prog/gpt4/a.txt


if [[ "$1" = "--noconfirm" || "$1" = "-i" ]]; then
	if [ "$1" = "-i" ]; then
		cp $2 $target_file
	fi

elif [ "$1" = "-f" ]; then
	cp $2 $target_file
	nano $target_file

else
	nano $target_file
fi


cd ~/prog/gpt4
$llm_exec
