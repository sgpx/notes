#!/bin/bash
yasm -f elf64 -o a.o a.s
ld -m elf_x86_64 -o a.out a.o

valgrind --quiet ./a.out
echo "exit code is $?"

if [ "$1" = "-noclean" ]; then
	exit
fi

rm *.o *.out
