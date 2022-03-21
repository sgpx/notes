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

- most significant bit = bit furthest to left = bit at the start = sign bit

- most significant bit is used to store the sign of number

- addition subtraction is complicated

- most integer CPUs do not support sign magnitude representation for addition, etc

- sign magnitude representation is commonly used for mantissa in floating point numbers

- mantissa = fractional part of floating point number

- characteristic = integer part of floating point number

- has two representations of zero which can cause problems

# excess representation

- stored number is N greater than its actual value

- (stored number) = (actual value) + N

- N = 2^(n-1) where n is the number of bits 

- easy to interpret

- example:

```
4-bit system

n = 4
N = 2**(4-1) = 2**3 = 8 = 1000

stored_number(0) = actual_value(0) + 1000
stored_number(0) = 0 + 8 = 8 = 1000

stored_number(-1) = -1 + 8 = 7 = 0111

stored_number(-2) = -2 + 8 = 6 = 0110

stored_number(-4) = -4 + 8 = 4 = 0100

stored_number(-8) = -8 + 8 = 0 = 0100

stored_number(1) = 1 + 8 = 9 = 1001

stored_number(2) = 2 + 8 = 10 = 1010

stored_number(4) = 4 + 8 = 12 = 1100

stored_number(7) = 7 + 8 = 15 = 1111

```
