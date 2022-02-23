segment .data
	msg db "Hello World", 0

segment .text
global _start

extern printf
extern ExitProcess

_start:
	lea rcx, [msg]
	call printf

	call ExitProcess
