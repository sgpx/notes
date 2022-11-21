.section .rodata
mesg: .asciz "Hello World\n" 

.global _main

_main:
	mov w0, #0
	ret
