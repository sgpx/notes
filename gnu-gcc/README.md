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

# building gcc from source

- needs GMP, MPFR and MPC
- use `./configure --disable-multilib` to only build 64bit compiler libraries and not 32bit
- is written in c++ and requires `g++` to build itself

# compile and install to preset root

``` 
mkdir cstinstall && mkdir cstinstall/bin cstinstall/lib cstinstall/lib64 cstinstall/include;
extract_source_tarball_archives; # extract dependencies to folders
export myprefix="$HOME/cstinstall";
export PATH="$myprefix/bin:$PATH";
cd m4 && ./configure --prefix=$myprefix && make -j20 && make install && cd .. 
cd gmp && ./configure --prefix=$myprefix && make -j20 && make install && cd ..
cd mpfr && ./configure --prefix=$myprefix --with-gmp=$myprefix && make -j20 && make install && cd ..
cd mpc && ./configure --prefix=$myprefix --with-gmp=$myprefix --with-mpfr=$myprefix && make -j20 && make install && cd ..
cd gcc && ./configure --prefix=$myprefix --with-gmp=$myprefix --with-mpfr=$myprefix --with-mpc=$myprefix --disable-multilib && make -j20 && make install && cd ..
```

