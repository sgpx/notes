# GNU GCC

# see expanded macros

```
gcc -E foo.c
```

# output assembly instructions only

```
gcc -S foo.c
```

# create shared library object

`-fpic` = position independent code

```
gcc -shared -fpic libxyz.c -o libxyz.so
```

# compile object without linking (preprocess+compile+assemble only)

```
gcc -c foo.c -o foo.o
```

# link object to shared library to produce executable

```
LD_LIBRARY_PATH="/home/user/" gcc a.o -test a.out libxyz.so
```
# gcc link math.h

`gcc a.c -lm`

# error

```
$ gcc a.c
/usr/bin/ld: /tmp/cc0udBUM.o: in function `main':
a.c:(.text+0x6a4): undefined reference to `sin'
/usr/bin/ld: a.c:(.text+0x6c4): undefined reference to `exp'
/usr/bin/ld: a.c:(.text+0x6e8): undefined reference to `pow'
```
