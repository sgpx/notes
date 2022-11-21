#!/bin/bash
a=$(ls *.java | sort -n | tail -n1 | sed -r "s/.java//")
echo "javac $a.java && java $a"
javac $a.java && java $a
printf "\n\n"
echo clearing
rm -v *.class
