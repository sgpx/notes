.data 0
mesg: .asciz "hello\n"

.text
.global main

main:
	adr x0, mesg
	b printf

	mov w0, #0
	ret
