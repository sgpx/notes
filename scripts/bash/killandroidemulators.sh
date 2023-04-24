#!/bin/bash
for i in $(ps -e | grep -E "qemu-system-.+(avd|\@)" | sed -r "s/^([0-9]+) .+/\1/"); do 
	echo $i; 
	kill -9 $i; 
done
