section .text
global _start
_start:
	; ssize_t write(int fd, const void * buf, size_t count)
	mov rax, 1 ; write(2) syscall
	mov rdi, 1 ; paramter 1 "fd" moved into "rdi"
	mov rsi, msg ; parameter 2 "buf" moved into "rsi"
	mov rdx, 11 ; parameter 3 "count" moved into "rdx"
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

section .data
msg db "hello world"
