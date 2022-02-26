section .text
global _start
_start:

	mov rax, [rip]
	mov rdi, 0
	syscall

section .data
msg db "hello world",10
len equ 12
