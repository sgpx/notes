section .text
global _start
_start:
	mov rax, 12
	cmp rax, 13
	je is_equal
	; if RAX equals 12 then jump to "is_equal"


	mov rax, 1
	mov rdi, 1
	mov rsi, msg_unequal
	mov rdx, len
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

is_equal:
	mov rax, 1
	mov rdi, 1
	mov rsi, msg_equal
	mov rdx, len
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

section .data
	msg_equal db "numbers are equal",10
	msg_unequal db "numbers are not equal",10
	len equ 25
