# mingw-w64

Minimalist GNU for Windows (64-bit)

# GCC windows target flags

https://gcc.gnu.org/onlinedocs/gcc/x86-Windows-Options.html

# statically compile a gui application

use flag `-mwindows` from above to specify the windows GUI subsystem for the application

```batch
g++ -static -static-libgcc -mwindows "%1%.cpp" -o "%1%.exe"
```

# generate a dll

use `-mdll`