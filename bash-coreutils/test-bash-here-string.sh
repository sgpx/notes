#!/bin/bash
bash --version

test_str="1_2"
IFS="_" read -a tmp <<< $test_str

for i in {0..2};
	do echo tmp$i ${tmp[$i]};
done
