#!/bin/bash
engine="gpt4.sh"
topic="numpy"

echo "I am learning $topic by example. I don't know $topic very well. this is all the work I have done so far: " > ~/tmp.txt
for a in $(ls a*.py); do echo $a >> ~/tmp.txt ; echo === >> ~/tmp.txt ; cat $a >> ~/tmp.txt ; echo === >> ~/tmp.txt ;  done
echo "${date} based on this data, what should I learn next? give me only 1 topic or exercise in 1-2 lines or less. the topic should be a direct continuation of what I have learned so far. based on this topic give me a highly practical yet challenging problem that can cause me to learn more about it. also give something that I should learn and then solve the problem with if possible" >> ~/tmp.txt
mv ~/tmp.txt ~/prog/gpt4/a.txt
$engine --noconfirm
