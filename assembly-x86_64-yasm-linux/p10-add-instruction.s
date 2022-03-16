global _start

_start:
	mov rdi, 1
	add rdi, 10
	mov rax, 60
	syscall
