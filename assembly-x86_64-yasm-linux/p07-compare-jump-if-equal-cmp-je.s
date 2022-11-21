section .text
global _start
_start:
	mov rax, 12
	cmp rax, 12
	je lol
	; if RAX equals 12 then jump to "lol"

	mov rax, 60
	mov rdi, 0
	syscall

lol:
	mov rax, 60
	mov rdi, 1
	syscall
