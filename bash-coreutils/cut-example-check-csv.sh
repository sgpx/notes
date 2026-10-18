#!/bin/bash
sort -n a.csv | uniq | tee a.bak
mv a.bak a.csv
IFS=$'\n'; 
j=4; 
for i in $(cut -d , -f 3 res.txt  | sort -n | sed -r "s/ //g"); do
	echo "i: $i, j: $j";
	if [ "$i" = "$j" ]; then 
		echo OK; 
	else
		break; 
	fi; 
	j=$(expr $j + 1); 
done
