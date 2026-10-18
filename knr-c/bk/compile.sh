#!/bin/bash
fn=$(ls *.c | sort -n | tail -n1);
echo "compiling $fn..";
echo "gcc $fn && ./a.out";
gcc $fn && ./a.out;

