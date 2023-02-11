# gdb

gnu debugger

# create debugging information with gcc

use `gcc -g`

```
 -g  Produce debugging information in the operating system's native format (stabs, COFF, XCOFF, or DWARF).  GDB can work
           with this debugging information.
```

`gcc -g a.c && gdb ./a.out`

# make breakpoint

`b main`

`b 9` for line 9

# start debugging

`start`

# go to next line

`next`

# use ncurses-based TUI mode

use [Ctrl] + [X] + [A]

# use python interpreter

```
(gdb) python
>import platform
>print(platform.python_version())
>end
3.10.6
```

# ref

- [Debugging with GDB, the GNU source level debugger](https://www.eecs.umich.edu/courses/eecs373/readings/Debugger.pdf) by R. Stallman, Pesch and Shebs
