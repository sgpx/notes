#!/bin/bash
function r() {
	rm a.out
	a=$(ls *.cpp | sort -n | tail -n1)
	echo running $a
	clang++ -std=c++20 $a -o a.out
	./a.out
}

function e() {
	x=$(ls *.cpp | sort -n | tail -n1)
	nano $x
}


function n() {
	x=$(ls *.cpp | sort -n | tail -n1)
	a=$(sed -r "s/a(.+)\.cpp/\1/" <<< "$a")
	b=a$(printf "%02d" $(expr $a '+' 1)).cpp
	cp -v $x $b
	nano $b
}

function h() {
	nano README.md
}
