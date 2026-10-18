# objdump

displays info about executable and object files

on mac, points to llvm-objdump

on linux, points to objdump from gnu-binutils

# mac example

`objdump --disassemble-all --macho --all-headers a.out`

# linux example

`objdump -x a.out`
