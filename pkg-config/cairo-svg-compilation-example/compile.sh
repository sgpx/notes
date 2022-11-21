#!/bin/bash
pkg-config --list-all | grep -i cairo-svg
echo "linker options (--libs) === $(pkg-config --libs cairo-svg)"
echo "compiler flags (--cflags) === $(pkg-config --cflags cairo-svg)"
echo gcc $(pkg-config --cflags cairo-svg) foo.c $(pkg-config --libs cairo-svg) -o foo.out
gcc $(pkg-config --cflags cairo-svg) foo.c $(pkg-config --libs cairo-svg) -o foo.out
echo ./foo.out
./foo.out
