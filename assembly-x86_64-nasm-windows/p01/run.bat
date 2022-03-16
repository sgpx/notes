nasm -f win64 -o x.obj x.asm 
link.exe x.obj /subsystem:console /entry:_start /out:x.exe kernel32.lib legacy_stdio_definitions.lib ucrt.lib /largeaddressaware:no 
