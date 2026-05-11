#!/bin/bash
for i in $(ls *cu); do printf "summarize in 1 line:\n\n" > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo cuda/${i},$(qwen25.sh --noconfirm) ; done
