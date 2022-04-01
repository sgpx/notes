.data
fmt:
	.string "num is %d\n"

.text
.global main
main:
	adr x0, fmt
	mov w1, #44
	b printf

	mov w0, #0
	ret
