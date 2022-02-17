global _start

_start:
	exit_code equ 42                  ;defining constants
	linux_syscall_terminate equ 60
	mov rax, linux_syscall_terminate
	mov rdi, exit_code
	syscall
