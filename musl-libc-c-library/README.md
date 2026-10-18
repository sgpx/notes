# musl

small C library for static linking

# build from source

```
./configure --prefix=$install_dir
make -j5
make install
```

# call a program using libc.so

```
cd $install_dir
./bin/musl-gcc a.c -o a.out
./lib/libc.so a.out
```
