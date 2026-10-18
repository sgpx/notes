#!/bin/bash
target="xyz.txt"
IFS="," read -ra arr <<< $(tail -n1 $target)
xsel -b <<< "${arr[0]}"
echo field1
echo OK
read
xsel -b <<< "${arr[1]}"
echo field2
echo OK
read
xsel -b <<< "."

