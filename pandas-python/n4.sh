#!/bin/bash

ctr=0
ctrfile="en4-ctr.txt"
        
LLM=nvidia-nemotron-ultra.sh 

# Read counter if exists
if [[ -f "$ctrfile" ]]; then
    ctr=$(<"$ctrfile")
fi

# If last argument is --next, increment counter
if [[ "${!#}" == "--next" ]]; then
    ctr=$((ctr+1))
fi

# Write counter back
echo "$ctr" > "$ctrfile"

# Get the line from ref2.txt
z=$(sed -n "$((ctr+1))p" ref2.txt)

echo "$z"

if [[ "$1" != "--question" && "$1" != "-q" && "$1" != "--check" ]]; then
# Run first oai-gpt41-nano command
	$LLM -p "explain ${z} with lots of examples but in a less text-dense way to explain to a student with low attention span. use markdown code blocks" > tmp.txt
	vbx.sh -f tmp.txt

# Set file paths
	cwd="$(pwd)/en4-ex-${ctr}.txt"
	target="$HOME/vbx-tmp.txt"

# Copy the file
	cp "$target" "$cwd"

	read -p "press any key for question"

fi

if [[ "$1" != "--check" ]] ; then
# Run second oai-gpt41-nano command
	level="easy"
	if [ "$2" != "" ]; then level="$2" ; fi
	$LLM -p "create an $level learning problem that can be solved with pandas ${z}" > tmp.txt
	vbx.sh -f tmp.txt

	cwd="$(pwd)/en4-pr-${ctr}.txt"
	target="$HOME/vbx-tmp.txt"

	cp "$target" "$cwd"
	cp "$target" curr.md
else
	echo "check the solution for the problem" > ~/tmp.txt
        a=$(ls ex*.py | sed -r "s/ex([0-9]+)\.py/\1/" | sort -n | tail -n1)
	echo checking ex${a}.py
	cat curr.md >> ~/tmp.txt
	printf "\n\nthis is the real solution created by the student, ignore the provided solution\n\n" >> ~/tmp.txt
	cat ex$a.py >> ~/tmp.txt
	$LLM -i ~/tmp.txt
fi


