#!/bin/bash
a=$(ls *.java | sort -n | tail -n1 | sed -r "s/.java//" | sed -r "s/p//")
echo $a
b=$(expr "$a" "+" "1")
d=$(printf "p%02d" "$b")
c="$d.java"
echo $c
touch $c

echo "class $d {" > $c
printf "\tpublic static void main(String[] args){\n\n\n\t}\n" >> $c
echo "}" >> $c

nano $c
