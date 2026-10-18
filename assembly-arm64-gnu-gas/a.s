.text
.global _main

_main:
    // Load two integers into registers
    mov x1, #11        // Load the first number (5) into x1
    mov x2, #10       // Load the second number (10) into x2

    // Add the two numbers
    add x16, x1, x2    // Add x1 and x2, store the result in x16

    // Exit the program (Linux specific way to exit)
    mov x8, #93       // syscall number for exit
    mov x16, #0        // exit code 0
    svc #0 
