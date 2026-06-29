#!/bin/bash
LLM=qwen25.sh
ext=md
lockpath="$HOME/prog/mluniv"
LLM_INPUT_FILE=~/prog/gpt4/a.txt

function get_date_string() {
	stat -f "%SB" $1
}

if [ "$(pgrep -f -i ollama)" = "" ]; then ollama serve & fi
if [ "$1" = "-s" ]; then
	lockfile="$lockpath/$(basename $PWD).md"
	if [ ! -r $lockfile ]; then echo "filename,description,creation_date" > $lockfile ; fi
	for curr_file in $(ls *.$ext); do chk=$(grep "${curr_file}," $lockfile) ; if [ "$chk" != "" ]; then echo "skipping $curr_file" ; continue ; else echo summarizing $curr_file ; fi ; printf "summarize in 1 line:\n\n" > $LLM_INPUT_FILE ; cat $curr_file >> $LLM_INPUT_FILE ; echo $(basename $PWD)/${curr_file},$($LLM --noconfirm),$(get_date_string $curr_file) >> $lockfile ; tail -n1 $lockfile ; done
else
	echo "filename,description,creation_date"
	for curr_file in $(ls *.$ext); do printf "summarize in 1 line:\n\n" > $LLM_INPUT_FILE ; cat $curr_file >> $LLM_INPUT_FILE ; echo $(basename $PWD)/${curr_file},$($LLM --noconfirm),$(get_date_string $curr_file) ; done
	if [ $(pgrep -f -i ollama) ! = "" ]; then kill -9 $(pgrep -f -i ollama) ; fi
fi
