; use strace to see full exit code
; ./compile.sh -noclean && strace ./a.out && echo $?
global _start

_start:
	rdrand rdi

	mov rax, 60
	syscall
