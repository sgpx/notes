#!/bin/bash

echo "int main(){ return 0; }" > test.c
cc test.c -o a.out
cat a.out | file -
