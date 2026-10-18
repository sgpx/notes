#!/bin/bash
# -fpic => position independent code
export LD_LIBRARY_PATH=$(realpath .)

gcc -shared -fpic libxyz.c -o libxyz.so

gcc -c a.c -o a.o

gcc a.o -o test.out libxyz.so

./test.out

rm *.o *.so *.out
