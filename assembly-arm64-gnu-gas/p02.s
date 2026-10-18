.global main

blah:
	mov w1, #1
	mov w2, #2
	mov w3, #0
	add w3, w1, w2
	b exit

exit:
	mov w0, w3
	ret

main:
	b blah
