# arm64 / aarch64 assembly notes

# programs

executable computer program = series of numbers

human readable program ---> stream of numbers

assembly -> machine code

instruction stream -> list of instructions for computer

instructions are executed sequentially

# memory

series of boxes

each box has its own unique identifier

each box can hold one number

cpu can put a number into a box

# registers

cpu has its own set of boxes

data can be copied from memory boxes to cpu boxes

Program Counter (PC) register keeps track of location of next instruction

# cpu sequence

1. fetch instruction from memory
2. increment program counter
3. execute instruction
4. repeat

some instructions can change the program counter so that next instruction is fetched from non sequential address

# uses of assembly

- booting the computer
- handling interrupts
- locking code for multithreaded programs
- when compiler generated assembly is not good enough
- low memory or no memory management
- code that requires access to low level processor or architecture features

- designing compilers
- using SIMD
- using vector instructions for arrays
- device drivers

- debugging
- advanced concepts like scheduling, out of order execution, threading, branch prediction, speculative execution

# SIMD

single instruction multiple data instruction

CPU can operate on multiple items of data at once

# data

binary digit = bit

bit = 0 or 1

bits are combined to represent numbers larger than 1

n-bits can represent numbers from 0 to (2^n)-1

# number bases

decimal = x base 10
binary = x base 2

octal = x base 8
hexadecimal = x base 16

# integer representation

four types

- unsigned
- sign magnitude
- excess 127 or excess (2^(n-1) - 1) 
- two's complement

# sign magnitude representation

most significant bit = bit furthest to left = bit at the start = sign bit

most significant bit is used to store the sign of number

addition subtraction is complicated
