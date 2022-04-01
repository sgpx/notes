.data
msg: .asciz "hello\n"

.text
.global _main

_main:
	adrp x0, msg@PAGE
	add x0, x0, msg@PAGEOFF
	b _printf

	mov w0, #0
	ret
