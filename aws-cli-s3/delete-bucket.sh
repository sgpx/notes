#!/bin/bash
fn="$1"
if [ "$fn" = "" ]; then echo error: empty input; exit; fi

function xyz(){
	a="$1";
	b="s3://$a"
	echo $b
	c=$(aws s3 ls $b | sed -r "s/^.+ (.+)$/\1/")
	d=$(grep -E "^.+/$" <<< "$c")

	for i in $c; do 
		echo $i; 
		if [ "$d" = "" ]; then 
			aws s3 rm "$b/$i";
		else 
			aws s3 rm --recursive "$b/$i";
		fi
		echo aws s3 rm $e "$b/$i";
	done
	aws s3 rb $b
}

fl=$(aws s3 ls | sed -r "s/^.+ (.+)/\1/" | grep -E "^$fn")
echo fl : $fl
for i in $fl; do
	xyz $i;
done

