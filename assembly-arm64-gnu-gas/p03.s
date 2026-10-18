.section .rodata

msg:
	.asciz "Hello ARM!\n"

.text

.global _main

_main:
	adr x0, msg
	b printf

	mov w0, #0
	ret	
