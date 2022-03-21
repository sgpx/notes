# otool

displays parts of binaries

preferred tool for inspecting Mach-O binaries

# print shared libraries

```
$ otool -L "$(which bash)"
/bin/bash:
	/usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1292.120.1)
$ otool -L "$(which clang)"
/usr/bin/clang:
	/usr/lib/libxcselect.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1292.120.1)
$ otool -L "$(which python3)"
/opt/homebrew/bin/python3:
	/opt/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/Python (compatibility version 3.9.0, current version 3.9.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1292.100.5)
```

`libSystem.B.dylib` is macos C standard library

# print mach header

```
$ otool -h /bin/zsh
/bin/zsh:
Mach header
      magic  cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
 0xfeedfacf 16777228          2  0x80           2    19       1896 0x00200085
```
