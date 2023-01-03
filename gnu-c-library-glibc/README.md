# building from source

1. download from ftp.gnu.org/gnu/glibc
2. extract to folder1/
3. go to folder2/
4. from folder2 run /path/to/folder1/configure
5. `make && make install`

# GLIBCXX ABI relation

https://gcc.gnu.org/onlinedocs/libstdc++/manual/abi.html

e.g. `GCC 7.2.0: GLIBCXX_3.4.24, CXXABI_1.3.11`

# GLIBCXX target

GLIBCXX versions can be found inside /usr/lib/libstdc++.so.*

`grep -i glibcxx /usr/lib/libstdc++.so.6`
