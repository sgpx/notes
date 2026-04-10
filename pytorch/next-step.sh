#!/bin/bash
txt=~/prog/gpt4/a.txt
echo 'i am trying to learn pytorch and neural networks. this is my existing knowledge. this is the current problem statement i am trying to solve' > $txt
echo === >> $txt
cat curr.md >> $txt
echo === >> $txt


if [ "$1" = "--skip" ]; then
echo "skipping"
else
echo "this is the current knowledge i have" >> $txt

a=$(find . -iname "*.py" -maxdepth 2)

for i in $a; do
	if [ "$i" = "curr.py" ]; then continue ; fi
	echo === >> $txt
	echo "# $i" >> $txt  ;
	cat $i >> $txt ;
	echo === >> $txt
done

fi

echo "this is the current solution i have" >> $txt
echo === >> $txt
cat curr.py >> $txt
echo === >> $txt

echo 'what do i write next? assuming i dont know much


based on my knowledge, tell me what mistakes exist in the program. make a bullet point list of mistakes vs. concepts/functions that i need to
go through first

dont write the code itself. dont solve the problem for me. do not write dense paragraphs (only 1 line per bullet point)
' >> $txt

cat ~/tmp.txt

IFS=$'\n'

cp -v $txt ~/tmp.txt
converse-gpt4o.sh -f

exit 0

gpt4.sh --noconfirm > ~/tmp.txt

for i in $(cat ~/tmp.txt); do
	echo $i
	oai-gpt41-nano.sh -p "explain this concept for learning pytorch with examples: $i" --qmd ;
	echo "press any key"
	read
done
