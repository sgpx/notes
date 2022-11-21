#!/bin/bash
if [ "$(uname -s)" = "Darwin" ]; then
	echo aliasing gcc
	alias gcc=/opt/homebrew/bin/gcc-11
fi
gcc --version
which gcc

echo compiing shared object
echo gcc -shared -fpic libxyz.c -o libxyz.so
gcc -shared -fpic libxyz.c -o libxyz.so

echo running preprocess+compile+assemble steps
echo gcc -c a.c -o a.o

echo linking object with shared object
echo gcc a.o libxyz.so -o test.out
gcc a.o libxyz.so -o test.out

echo running output binary
echo ./test.out
echo ====
./test.out
echo ====

echo cleaning up
rm *.o *.so *.out
