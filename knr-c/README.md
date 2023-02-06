# scanf behavior

using test program

```
#include <stdio.h>

int main(){
	int x = 0, y = 0, z = 0;
	scanf("%d_%d_%d,", &x, &y, &z);
	printf("x : %d, y : %d, z : %d\n", x, y, z);
	return 0;
}
```

```
$ ./a.out # perfect match
1_2_3,
x : 1, y : 2, z : 3

$ ./a.out # does not care about characters after format has no more format strings left
1_2_3
x : 1, y : 2, z : 3

$ ./a.out # collects inputs only until input format is valid
1_2 3,
x : 1, y : 2, z : 0

$ ./a.out
1 2 3,
x : 1, y : 0, z : 0
```

```
// does not work as intended because immediately after second int it looks for a character and gets '\n' or ' ' or '\0' or EOF

#include <stdio.h>

int main()
{
	int nc = 0, nd = 0, ne = 0;
	scanf("%d", &nc);
	scanf("%d", &nd);
	scanf("%c", &ne);
	printf("nc : %d\n", nc);
	printf("nd : %d\n", nd);
	printf("ne : %c\n", ne);
}


```

# stdarg.h

contains macros for unnamed function arguments

```
#include <stdarg.h>

void fxn(int a, int b, ...){
	va_list ap;
	va_start(ap, b); // points to first unnamed arg, takes last named arg as argument
	i = va_arg(arg, dt); // gets argument of datatype dt;
	va_end(ap); // cleanup
}

```

# unistd.h

unistd.h is the name of the header file that provides access to the POSIX operating system API

# system calls

mac os

https://opensource.apple.com/source/xnu/xnu-201/bsd/sys/errno.h

https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html

https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/open.2.html

https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/stat.2.html

https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/write.2.html

linux

https://man7.org/linux/man-pages/man2/open.2.html

https://man7.org/linux/man-pages/man2/read.2.html

https://man7.org/linux/man-pages/man2/stat.2.html

https://man7.org/linux/man-pages/man2/write.2.html

https://linux.die.net/man/2/stat

# casting `malloc()`

K&R and pre-1989 C uses casts for malloc. C++ also requires use of casting malloc()

https://stackoverflow.com/questions/20094394/why-do-we-cast-return-value-of-malloc

https://stackoverflow.com/questions/605845/do-i-cast-the-result-of-malloc

# type qualifier

`const` : value cannot change once initialized

```
const unsigned int x = 5;
// [type_qualifier] [type_specifier] [type_specifier] [name]
```

# const pointer syntax

ref : Appendix A.8.5

```
int main(){
	int z = 1;
	int const *y = &z;
	int const * const *x = &y;
	int const * const * xyz = x;
}
```


```
	// gives duplicate const warning
	const int z = 1;
	const int const * y = &z;
```
# entab detab problem

refer to manpage for [tabs](https://www.freebsd.org/cgi/man.cgi?query=tabs)

# output to stderr

```
#include <stdio.h>

int main(){
	x = 10;
	fprintf(stderr, "x : %d\n", x);
	return 0;
}
```

# array name is address of first value

```
int x[3] = { 1, 2, 3 };
printf("%p\n", x);
printf("%p\n", &x[0]);

printf("%p\n", x+2);
printf("%p\n", &x[2]);
```

# `*` (value at address) and `&` (address of) operators

```
int x = 1;
int * y = &x; // equals address of x in memory
int z = * y; // equals 1
```

# NUL terminated strings

`char x[3] = "abc"`

# printf()

first argument is string of characters to be printed

each `%` denotes a spot where the next arguments are to be substituted into

`%d` => integer argument, decimal integer

`%6d` => decimal integer 6 characters wide

`%f` => floating point number

`%6f` => floating point, 6 characters wide

`%.2f` => floating point, 2 characters wide

`%6.2f` => floating point, 6 characters wide, at least 2 digits after decimal point ("1234.56")

`%3.0f` => floating point, 3 characters wide, 0 characters after decimal point 

`%lu` => unsigned long int

`%p` => pointer address

```
printf("%f\n",12345.6798);
//outputs 12345.679800

printf("%6.2f\n",12345.6798);
//outputs 12345.68

printf("%3.0f\n",12345.6798);
//12346

printf("%3.1f\n",123.45);
//123.5
```
# `getchar()`

returns integer value of next input character

newline is also counted as an input

# `putchar(c)`

outputs character value of integer c

# EOF

EOF is usually passed to getchar() by [CTRL] + [D]

# memset

include `<string.h>`

```c
char a[100];
memset(a,'x',sizeof(a));

int b[50];
memset(b,999,sizeof(b));

```
# char from octal sequence 

```c
char c = '\000';
```

# char from hexadecimal sequence 

```c
char c = '\x5F';
```

# data type sizes

`char` -> 1 byte, capable of holding 1 character

`int` -> natural size of integers on host machine

# ===

don't use `clang-format`

# ===

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

# declarator grammar

declarator:
- `pointer^opt direct_declarator`

direct declarator:
- `identifier`
- `(declarator)`
- `direct_declarator[constexpr]`
- `direct_declarator(parameter_type_list)`

pointer:
- `type_qualifier_list^opt`
- `type_qualifier_list^opt pointer`

type_qualifier_list:
- `type_qualifier`
- `type_qualifier_list type_qualifier`

----

```
dcl -> pointer* dirdcl

dirdcl -> (dcl)
dirdcl -> ident
dirdcl -> dirdcl[constexpr]
dirdcl -> dirdcl(param_type_list)

pointer -> asterisk type_qualifier_list*
pointer -> asterisk type_qualifier_list* pointer

type_qualifier_list -> const
type_qualifier_list -> volatile
```

# (make dcl recover from input errors)

## error 1 

```
>>> int x(
syntax error
>>> int x()
int :
```

happens because the new gettoken() call is made inside the previous dcl() call
