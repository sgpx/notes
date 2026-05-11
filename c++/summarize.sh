#!/bin/bash
for i in $(find . -iname "*.cpp"); do printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo $(basename $PWD)/${i},$(qwen25.sh --noconfirm) ; done
