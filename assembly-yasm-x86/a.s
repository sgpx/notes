global _start

_start:
	rdrand rdi

	mov rax, 60
	syscall
