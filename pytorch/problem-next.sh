#!/bin/bash
engine="gpt4.sh"
echo "I am learning pytorch by example. I don't know neural networks very well. this is all the work I have done so far: " > ~/tmp.txt
for a in $(ls ex*.py); do echo $a >> ~/tmp.txt ; echo === >> ~/tmp.txt ; cat $a >> ~/tmp.txt ; echo === >> ~/tmp.txt ;  done
#echo "I feel like I should go back and study math first because this stuff seems not very useful to me. what should I study?" >> ~/tmp.txt
echo "based on this data, what should I learn next? give me only 1 topic or exercise in 1-2 lines or less. the topic should be a direct continuation of what I have learned so far. based on this topic give me a highly practical yet challenging problem that can cause me to learn more about it" >> ~/tmp.txt
mv ~/tmp.txt ~/prog/gpt4/a.txt
$engine --noconfirm
