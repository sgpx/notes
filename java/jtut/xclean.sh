#!/bin/bash
for i in $(find . -iname "*.class" -depth); do
	echo removing $i;
	rm -v $i;
done;
for i in $(find . -iname "*.jar" -depth); do
	echo removing $i;
	rm -v $i;
done;
