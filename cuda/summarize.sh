#!/bin/bash
if [ $(pgrep -f -i ollama) ]; then ollama serve & fi
for curr_file in $(ls *.cu); do printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $curr_file >> ~/prog/gpt4/a.txt ; echo $(basename $PWD)/${curr_file},$(stat -f "%SB" $curr_file),$(qwen25.sh --noconfirm) ; done
kill -9 $(pgrep -f -i ollama)
