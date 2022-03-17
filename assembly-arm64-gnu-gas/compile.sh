#!/bin/bash
platform=$(uname -s)

if [ "$1" != "" ]; then
	cp -v $1 a.s
fi

if [ "$platform" = "Darwin" ]; then
	if [ "$(grep _main a.s)" = "" ]; then
		sed -i "" -r "s/main/_main/g" a.s
	fi
	clang -o a.out a.s
	./a.out
else
	sed -i "" -r "s/_main/main/g" a.s
	gcc -o a.out a.s
	./a.out
fi


echo exit code: $?
