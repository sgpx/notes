.data
ascii_1: .word 0x31
ascii_2: .word 0x32
ascii_newline: .word 0x0A

.text
.global main
main:
	adr x0, ascii_1
	bl puts
	adr x0, ascii_2
	bl puts
	mov w0, #0
	ret
