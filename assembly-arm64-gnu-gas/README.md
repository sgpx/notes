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

# complement representation

- negative numbers are represented as complements of positive counterparts

- very efficient method of dealing with signed numbers

- most significant digit of number is reserved to indicate whether is number is negative

```
if most_significant_digit < (radix/2):
	sign = "positive"
else:
	sign = "negative"
```

- complement

```
complement(y, base=b, bits=n) = (b^n) - y
```

complement(0, base=2, bits=2) = 2**2 - 0 = 4 = 11


# character representation

ASCII = 7 bit code

33/128 = non printable control characters

95/128 = printable control characters

# memory layout

memory address are usually represented as hexadecimal

each location can contain fixed number of bits

most common size is 1 byte

computers group bytes into words

1 word = 2 bytes = 16 bits

computers that access memory through bytes = byte addressable

computers that access memory through words = word addressable

on 32-bit system, four bytes are stored together to form a word

BIG-ENDIAN SYSTEMS: store most significant byte of word in smallest address, store least significant byte in largest address

LITTLE-ENDIAN SYSTEMS: store most significant byte of word in largest address, store least significant byte of word in smallest address

linux by default configures ARM CPUs to run in little endian mode

# memory layout of program

each program contains following sections:

- `.data`
- `.rodata`
- `.text`
- `.bss`
-  stack
-  heap

stack and heap are defined when program is loaded for execution

`.data`, `.rodata`, `.bss` => contain static variables

size of `.text`, `.data`, `.rodata`, `.bss` depends on size of program and size of declared static storage by programmer

heap: contains variables allocated dynamically

stack: stores parameters for function calls, stores return addresses, stores local and automatically declared variables

in high level languages, storage space for variables can be allocated:

- statically => .data, .rodata, .bss; space is reserved and initialized when program begins execution
- dynamically => allocated on heap using `malloc()` `new` or similar equivalent
- automatically (local variables) => stored on stack, using an offset from stack pointer

# assembly program structure

four basic elements

- directives
- labels
- instructions
- comments

# assembly directives

allows programmer to:

- reserve memory for storage of variables

- control which program section is being used

- define macros

- include other files

- perform operations that control conversion of assembly instructions to machine code

# assembly instructions

- mnemonics

- short character sequences easy to remember instead of machine code

- most instructions require programmer to specify one or more operands

# labels

- modern assemblers make two passes through the program

- first pass keeps track of location of each piece of data or instruction, building a symbol table

- second pass assembly converts instructions to binary

- labels are used to refer to address of data, functions, etc

- in GAS, label declarations always end with `:` like `main:`

# directives

used to:

- define symbols
- allocate storage
- control the behavior of the assembler

all assembler directives begin with '.' e.g. `.data`, `.rodata`, `.section`

# BSS

block started by symbol

# `.size` directive

sets size associated with a symbol

COFF

`.size EXPRESSION`

ELF

`.size name, EXPRESSION`


# STP instruction

stores pair of registers

calculates address from a base register value and immediate offset

stores two 32-bit words or 64-bit doublewords to the calculated address

from two registers

into calculated address

# ADR instruction

```
adr register, expression
```

where expression evaluates to a non word-aligned address within 255 bytes 

or a word-aligned address 1020 bytes

# assembler process

first variable inside .data block is stored at address 0000

assembler declares defined and undefined values 

linker uses undefined value to patch in values from linked libraries like glibc 

# `.data` directive

`.data X` instructs assembler to append data to data subsections numbered X

if X is omitted it defaults to subsection number 0

`.data` is used for global variables and constants which have labels

# `.text` directive

`.text X` instructs assembler to append following statements to subsection 0

if X is omitted it defaults to 0

this section is used for instructions

# `.bss` directive

defines data storage areas that are initialized to zero at the start of program execution

used for global variables that need to be initialized to zero 

# `.section` direction

programmer can create extra subsections using the `.section` directive but needs to specify how to use those subsections using a linker script

# link register

`LR` or `R14`

`bl` instruction uses link register compared to `b` which does not use `LR`

special purpose register

holds address to return to when function call completes
