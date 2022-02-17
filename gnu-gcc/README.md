# GNU GCC

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
