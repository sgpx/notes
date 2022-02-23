section .text
global _start
_start:
	mov rdi, msg
	mov rax, 80
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

section .data
msg db "/"
len equ 9
