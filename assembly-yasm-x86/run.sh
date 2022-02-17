#!/bin/bash
yasm -f elf64 -o a.o a.s
ld -m elf_x86_64 -o a.out a.o

./a.out
echo "exit code is $?"

rm *.o *.out
