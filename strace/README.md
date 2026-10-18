# strace

trace system calls

# set syscall data line length

`strace -v -s 1024 ls`

# get failed system calls only

`strace -Z ls`

# attach timestamp

`strace --timestamps=unix ls`

# attach pid

`strace -p 123`

# attach all child processes

`2>output.txt strace -f wine a.exe`

`2>output.txt strace --follow-forks wine a.exe`


