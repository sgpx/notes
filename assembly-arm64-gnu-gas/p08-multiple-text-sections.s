.data
msg: .string "lmao\n"

.text 0
.global main
main:
	mov w0, #1
	bl secondblock
	ret

.text 1
secondblock:
	adr x0, msg
	b printf
	mov w0, #0
	ret
