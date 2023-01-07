# patchelf

set binary interpreter and runtime path (rpath) for ELF files

# install

`sudo pip3 install patchelf`

# print interpreter

`patchelf --print-interpreter a.bin`

# set interpreter

`patchelf --set-interpreter /lib64/ld-musl-x86_64_musl.so a.bin`

# print rpath

`patchelf --print-interpreter a.bin`

# set rpath

`patchelf --set-rpath /lib64/libc.so.6 a.bin`

# add rpath

`patchelf --add-rpath /lib64/libc.so.6 a.bin`

# add rpath

`patchelf --remove-rpath /lib64/libc.so.6 a.bin`



