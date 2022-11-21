#!/bin/bash
function myfunc(){
	echo arg1 is $1
	echo arg2 is $2
	argsum=$(expr "$1" "+" "$2")
	echo "expr '$1' '+' '$2' = $argsum"
}

myfunc 3 4
