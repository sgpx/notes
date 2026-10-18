#!/bin/bash
gcc -Wall a.c && valgrind -s --leak-check=full --track-origins=yes ./a.out
