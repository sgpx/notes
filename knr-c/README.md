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
