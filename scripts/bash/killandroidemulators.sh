#!/bin/bash
for i in $(ps -e | grep qemu | grep avd | sed -r "s/^([0-9]+) .+/\1/"); do 
	echo $i; 
	kill -9 $i; 
done
