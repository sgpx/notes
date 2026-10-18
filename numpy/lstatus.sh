#!/bin/bash
engine="gpt4.sh"
engine="claude3-sonnet.sh"
if [ -r a.txt ] ; then rm a.txt ; fi
printf "I am learning numpy. this is my progress in so far\n\n" >> a.txt

for i in $(ls a*.py); do
	echo === >> a.txt
	echo $(ls -l $i) >> a.txt
	echo === >> a.txt
	cat $i >> a.txt
done


printf "\n\n===\ntoday is ${date}\n\ncomment on my progress in terms of (bullet points) regularity and skill level. give me advice on what numpy functions/features I should explore next" >> a.txt

mv a.txt ~/prog/gpt4
$engine --noconfirm
