# `.data`

contains all the data used by the program

# `.rodata`

contains all the read only data used by the program

# `.text`

contains all code

# _start

every program must have a `global _start`

# register mapping for system call invocation using `syscall` instruction

system call number: `rax`
parameter 1: `rdi`
parameter 2: `rsi`
parameter 3: `rdx`
parameter 4: `r10`
parameter 5: `r8`
parameter 6: `r9`

result: `rax`

# write

`ssize_t write(int fd, const void * buf, ssize_t count)`

fd : file descriptor => `rdi` (1st parameter register for syscall instruction)

buf : buffer => `rsi` (2nd parameter register for syscall instruction)

count : number of bytes to write => `rdx` (3rd parameter register for syscall instruction)

# resources

linux system call parameter register list:

[https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux](https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux)

write(2):

https://man7.org/linux/man-pages/man2/write.2.html

syscall table:

https://filippo.io/linux-syscall-table/

introduction to x86_64 assembly with ubuntu, by ed jorgensen

http://www.egr.unlv.edu/~ed/x86.html

http://www.egr.unlv.edu/~ed/assembly64.pdf
