.data 0
mesg_one: .asciz "hello\n"

.data 1
mesg_two: .asciz "world\n"

.text
.global main

main:
	ret
