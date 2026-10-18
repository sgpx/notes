	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 11, 0	sdk_version 11, 3
	.globl	_alloc                          ; -- Begin function alloc
	.p2align	2
_alloc:                                 ; @alloc
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16                     ; =16
	.cfi_def_cfa_offset 16
	mov	x9, #5000
	adrp	x8, _allocbuf@PAGE
	add	x8, x8, _allocbuf@PAGEOFF
	add	x9, x8, x9
	str	w0, [sp, #4]
	adrp	x8, _allocp@PAGE
	ldr	x8, [x8, _allocp@PAGEOFF]
	ldrsw	x10, [sp, #4]
	add	x8, x8, x10
	subs	x8, x8, x9
	b.hs	LBB0_2
; %bb.1:
	ldrsw	x10, [sp, #4]
	adrp	x8, _allocp@PAGE
	ldr	x9, [x8, _allocp@PAGEOFF]
	add	x9, x9, x10
	str	x9, [x8, _allocp@PAGEOFF]
	ldr	x8, [x8, _allocp@PAGEOFF]
	ldrsw	x9, [sp, #4]
	subs	x8, x8, x9
	str	x8, [sp, #8]
	b	LBB0_3
LBB0_2:
	str	xzr, [sp, #8]
LBB0_3:
	ldr	x0, [sp, #8]
	add	sp, sp, #16                     ; =16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_afree                          ; -- Begin function afree
	.p2align	2
_afree:                                 ; @afree
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16                     ; =16
	.cfi_def_cfa_offset 16
	mov	x8, #5000
	adrp	x9, _allocbuf@PAGE
	add	x9, x9, _allocbuf@PAGEOFF
	add	x8, x9, x8
	str	x8, [sp]                        ; 8-byte Folded Spill
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
	subs	x8, x8, x9
	b.lo	LBB1_3
; %bb.1:
	ldr	x9, [sp]                        ; 8-byte Folded Reload
	ldr	x8, [sp, #8]
	subs	x8, x8, x9
	b.hi	LBB1_3
; %bb.2:
	ldr	x8, [sp, #8]
	adrp	x9, _allocp@PAGE
	str	x8, [x9, _allocp@PAGEOFF]
LBB1_3:
	add	sp, sp, #16                     ; =16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_numcmp                         ; -- Begin function numcmp
	.p2align	2
_numcmp:                                ; @numcmp
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64                     ; =64
	stp	x29, x30, [sp, #48]             ; 16-byte Folded Spill
	add	x29, sp, #48                    ; =48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-16]
	str	x1, [sp, #24]
	ldur	x0, [x29, #-16]
	bl	_atof
	str	d0, [sp, #16]
	ldr	x0, [sp, #24]
	bl	_atof
	str	d0, [sp, #8]
	ldr	d0, [sp, #16]
	ldr	d1, [sp, #8]
	fcmp	d0, d1
	b.pl	LBB2_2
; %bb.1:
	mov	w8, #-1
	stur	w8, [x29, #-4]
	b	LBB2_5
LBB2_2:
	ldr	d0, [sp, #16]
	ldr	d1, [sp, #8]
	fcmp	d0, d1
	b.le	LBB2_4
; %bb.3:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_5
LBB2_4:
	stur	wzr, [x29, #-4]
LBB2_5:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #64                     ; =64
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_x_getline                      ; -- Begin function x_getline
	.p2align	2
_x_getline:                             ; @x_getline
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48                     ; =48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32                    ; =32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	bl	_getchar
	sturb	w0, [x29, #-13]
	ldur	x8, [x29, #-8]
	str	x8, [sp, #8]
LBB3_1:                                 ; =>This Inner Loop Header: Depth=1
	ldursb	w8, [x29, #-13]
	subs	w8, w8, #10                     ; =10
	b.eq	LBB3_3
; %bb.2:                                ;   in Loop: Header=BB3_1 Depth=1
	ldurb	w8, [x29, #-13]
	ldur	x9, [x29, #-8]
	add	x10, x9, #1                     ; =1
	stur	x10, [x29, #-8]
	strb	w8, [x9]
	b	LBB3_1
LBB3_3:
	ldur	x8, [x29, #-8]
	strb	wzr, [x8]
	ldur	x8, [x29, #-8]
	ldr	x9, [sp, #8]
	subs	x8, x8, x9
	mov	x0, x8
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48                     ; =48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_readlines                      ; -- Begin function readlines
	.p2align	2
_readlines:                             ; @readlines
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-32]!           ; 16-byte Folded Spill
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16                    ; =16
	sub	sp, sp, #1056                   ; =1056
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w27, -24
	.cfi_offset w28, -32
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-24]
	str	x0, [sp, #32]
	str	w1, [sp, #28]
	str	wzr, [sp, #20]
; %bb.1:
	add	x0, sp, #48                     ; =48
	mov	w1, #1000
	bl	_x_getline
	str	w0, [sp, #24]
	subs	w8, w0, #0                      ; =0
	b.le	LBB4_7
; %bb.2:
	ldr	w0, [sp, #24]
	bl	_alloc
	str	x0, [sp, #8]
	ldr	w8, [sp, #20]
	ldr	w9, [sp, #28]
	subs	w8, w8, w9
	b.ge	LBB4_4
; %bb.3:
	ldr	x8, [sp, #8]
	cbnz	x8, LBB4_5
LBB4_4:
	mov	w8, #-1
	str	w8, [sp, #44]
	b	LBB4_8
LBB4_5:
	ldr	w8, [sp, #24]
	subs	w8, w8, #1                      ; =1
	add	x1, sp, #48                     ; =48
	add	x8, x1, w8, sxtw
	strb	wzr, [x8]
	ldr	x0, [sp, #8]
	mov	x2, #-1
	bl	___strcpy_chk
	ldr	x8, [sp, #8]
	ldr	x9, [sp, #32]
	ldrsw	x10, [sp, #20]
	mov	x11, x10
	add	w11, w11, #1                    ; =1
	str	w11, [sp, #20]
	add	x9, x9, x10, lsl #3
	str	x8, [x9]
; %bb.6:
	ldr	w8, [sp, #20]
	str	w8, [sp, #44]
	b	LBB4_8
LBB4_7:
	mov	w8, #-1
	str	w8, [sp, #44]
LBB4_8:
	ldr	w8, [sp, #44]
	str	w8, [sp, #4]                    ; 4-byte Folded Spill
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	ldur	x9, [x29, #-24]
	subs	x8, x8, x9
	b.ne	LBB4_10
; %bb.9:
	ldr	w0, [sp, #4]                    ; 4-byte Folded Reload
	add	sp, sp, #1056                   ; =1056
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #32             ; 16-byte Folded Reload
	ret
LBB4_10:
	bl	___stack_chk_fail
	.cfi_endproc
                                        ; -- End function
	.globl	_writelines                     ; -- Begin function writelines
	.p2align	2
_writelines:                            ; @writelines
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48                     ; =48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32                    ; =32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	str	wzr, [sp, #16]
LBB5_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #16]
	ldur	w9, [x29, #-12]
	subs	w8, w8, w9
	b.ge	LBB5_4
; %bb.2:                                ;   in Loop: Header=BB5_1 Depth=1
	ldur	x8, [x29, #-8]
	ldrsw	x9, [sp, #16]
	ldr	x8, [x8, x9, lsl #3]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
; %bb.3:                                ;   in Loop: Header=BB5_1 Depth=1
	ldr	w8, [sp, #16]
	add	w8, w8, #1                      ; =1
	str	w8, [sp, #16]
	b	LBB5_1
LBB5_4:
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48                     ; =48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_swap                           ; -- Begin function swap
	.p2align	2
_swap:                                  ; @swap
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32                     ; =32
	.cfi_def_cfa_offset 32
	str	x0, [sp, #24]
	str	w1, [sp, #20]
	str	w2, [sp, #16]
	ldr	x8, [sp, #24]
	ldrsw	x9, [sp, #20]
	ldr	x8, [x8, x9, lsl #3]
	str	x8, [sp, #8]
	ldr	x8, [sp, #24]
	ldrsw	x9, [sp, #16]
	ldr	x8, [x8, x9, lsl #3]
	ldr	x9, [sp, #24]
	ldrsw	x10, [sp, #20]
	add	x9, x9, x10, lsl #3
	str	x8, [x9]
	ldr	x8, [sp, #8]
	ldr	x9, [sp, #24]
	ldrsw	x10, [sp, #16]
	add	x9, x9, x10, lsl #3
	str	x8, [x9]
	add	sp, sp, #32                     ; =32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_x_qsort                        ; -- Begin function x_qsort
	.p2align	2
_x_qsort:                               ; @x_qsort
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48                     ; =48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32                    ; =32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	str	w2, [sp, #16]
	str	x3, [sp, #8]
	ldur	w8, [x29, #-12]
	ldr	w9, [sp, #16]
	subs	w8, w8, w9
	b.lt	LBB7_2
; %bb.1:
	b	LBB7_9
LBB7_2:
	ldur	x0, [x29, #-8]
	ldur	w1, [x29, #-12]
	ldur	w8, [x29, #-12]
	ldr	w9, [sp, #16]
	add	w8, w8, w9
	mov	w9, #2
	sdiv	w2, w8, w9
	bl	_swap
	ldur	w8, [x29, #-12]
	str	w8, [sp]
	ldur	w8, [x29, #-12]
	add	w8, w8, #1                      ; =1
	str	w8, [sp, #4]
LBB7_3:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #4]
	ldr	w9, [sp, #16]
	subs	w8, w8, w9
	b.gt	LBB7_8
; %bb.4:                                ;   in Loop: Header=BB7_3 Depth=1
	ldr	x8, [sp, #8]
	ldur	x9, [x29, #-8]
	ldrsw	x10, [sp, #4]
	ldr	x0, [x9, x10, lsl #3]
	ldur	x9, [x29, #-8]
	ldursw	x10, [x29, #-12]
	ldr	x1, [x9, x10, lsl #3]
	blr	x8
	subs	w8, w0, #0                      ; =0
	b.ge	LBB7_6
; %bb.5:                                ;   in Loop: Header=BB7_3 Depth=1
	ldur	x0, [x29, #-8]
	ldr	w8, [sp]
	add	w1, w8, #1                      ; =1
	str	w1, [sp]
	ldr	w2, [sp, #4]
	bl	_swap
LBB7_6:                                 ;   in Loop: Header=BB7_3 Depth=1
; %bb.7:                                ;   in Loop: Header=BB7_3 Depth=1
	ldr	w8, [sp, #4]
	add	w8, w8, #1                      ; =1
	str	w8, [sp, #4]
	b	LBB7_3
LBB7_8:
	ldur	x0, [x29, #-8]
	ldur	w1, [x29, #-12]
	ldr	w2, [sp]
	bl	_swap
	ldur	x0, [x29, #-8]
	ldur	w1, [x29, #-12]
	ldr	w8, [sp]
	subs	w2, w8, #1                      ; =1
	ldr	x3, [sp, #8]
	bl	_x_qsort
	ldur	x0, [x29, #-8]
	ldr	w8, [sp]
	add	w1, w8, #1                      ; =1
	ldr	w2, [sp, #16]
	ldr	x3, [sp, #8]
	bl	_x_qsort
LBB7_9:
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48                     ; =48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #80                     ; =80
	stp	x29, x30, [sp, #64]             ; 16-byte Folded Spill
	add	x29, sp, #64                    ; =64
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	adrp	x8, _lineptr@GOTPAGE
	ldr	x8, [x8, _lineptr@GOTPAGEOFF]
	str	x8, [sp, #8]                    ; 8-byte Folded Spill
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	stur	wzr, [x29, #-24]
	ldur	w8, [x29, #-8]
	subs	w8, w8, #1                      ; =1
	b.le	LBB8_3
; %bb.1:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.1@PAGE
	add	x1, x1, l_.str.1@PAGEOFF
	bl	_strcmp
	cbnz	w0, LBB8_3
; %bb.2:
	mov	w8, #1
	stur	w8, [x29, #-24]
LBB8_3:
	ldr	x0, [sp, #8]                    ; 8-byte Folded Reload
	mov	w1, #5000
	bl	_readlines
	stur	w0, [x29, #-20]
	subs	w8, w0, #0                      ; =0
	b.le	LBB8_8
; %bb.4:
	adrp	x8, _numcmp@PAGE
	add	x8, x8, _numcmp@PAGEOFF
	str	x8, [sp, #32]
	adrp	x8, _strcmp@GOTPAGE
	ldr	x8, [x8, _strcmp@GOTPAGEOFF]
	str	x8, [sp, #24]
	ldur	w8, [x29, #-24]
	cbz	w8, LBB8_6
; %bb.5:
	ldr	x8, [sp, #32]
	str	x8, [sp]                        ; 8-byte Folded Spill
	b	LBB8_7
LBB8_6:
	ldr	x8, [sp, #24]
	str	x8, [sp]                        ; 8-byte Folded Spill
LBB8_7:
	ldr	x0, [sp, #8]                    ; 8-byte Folded Reload
	ldr	x8, [sp]                        ; 8-byte Folded Reload
	str	x8, [sp, #16]
	ldur	w8, [x29, #-20]
	subs	w2, w8, #1                      ; =1
	ldr	x3, [sp, #16]
	mov	w1, #0
	bl	_x_qsort
	ldr	x0, [sp, #8]                    ; 8-byte Folded Reload
	ldur	w1, [x29, #-20]
	bl	_writelines
	stur	wzr, [x29, #-4]
	b	LBB8_9
LBB8_8:
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	mov	w8, #1
	stur	w8, [x29, #-4]
LBB8_9:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #64]             ; 16-byte Folded Reload
	add	sp, sp, #80                     ; =80
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__DATA,__data
	.p2align	3                               ; @allocp
_allocp:
	.quad	_allocbuf

.zerofill __DATA,__bss,_allocbuf,5000,0 ; @allocbuf
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%s\n"

l_.str.1:                               ; @.str.1
	.asciz	"-n"

	.comm	_lineptr,40000,3                ; @lineptr
l_.str.2:                               ; @.str.2
	.asciz	"error: input too big\n"

.subsections_via_symbols
