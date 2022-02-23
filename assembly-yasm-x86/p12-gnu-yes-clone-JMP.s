section .text
global _start
_start:
	mov rdx, len
	mov rsi, msg
	mov rdi, 1
	mov rax, 1
	syscall

	jmp _start


section .data
msg db "y",10
len equ 2
