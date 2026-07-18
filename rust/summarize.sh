#!/bin/bash
for i in $(find . -type f -iname "*.rs" | sort -n | uniq); do printf 'summarize this program in 1 line:\n' > ~/prog/gpt4/a.txt ; cat $i >> ~/prog/gpt4/a.txt ; echo $i $(qwen25.sh --noconfirm) ; done
