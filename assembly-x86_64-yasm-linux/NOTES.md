# register bits/bytes hex representation

rax = (0000 0000 0000 0000)16

where each digit represents 1 byte made of 8 bits

each bit can represent a number from 0 to 255 

or 0 to (1111 1111)2 = (255)10

# data sizes

byte => 8 bits => 1 byte
word => 16 bits => 2 bytes
double word => 32 bits => 4 bytes
quad word => 64 bits => 8 bytes
double quad word => 128 bits => 16 bytes

# registers

temporary storage working location

built into the CPU itself

separate from memory

# general purpose registers

16 x 64bit general purpose registers

registers:

- rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp
- r8, r9, r10, r11, r12, r13, r14, r15

register subsets:

- rax (64bit) => eax (32bit) => ax (16bit) => al (8bit)
- ...
- r8 (64bit) => r8d (32bit) => r8w (16bit) => r8b (8 bit)

---

rax = 64bit register

eax = second half of rax (last 32 bits)

ax = second of eax (last 16 bits)

ah = first half of ax (first 8 bits)

al = second half of ax (last 8 bits)

# stack pointer register (RSP)

rsp points to top of the stack

# base pointer register (RBP)

rbp is used as base pointer during function calls

# instruction pointer register (RIP)

- special register used by CPU
- points to next instruction

