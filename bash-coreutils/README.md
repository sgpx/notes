# read

```bash
$ IFS="," read -a tmp <<< "a,b,c"
$ for i in {0..2}; do echo ${tmp[i]}; done
a
b
c
```

# sequences

```bash
$ echo {5..10}
5 6 7 8 9 10

$ echo {5..10}{1..4}
51 52 53 54 61 62 63 64 71 72 73 74 81 82 83 84 91 92 93 94 101 102 103 104
```

# arrays

arrays are space separated

```bash
$ myarray=(foo bar baz)
$ echo ${myarray[1]}
bar
```

# redirection

HERE-STRING: pass a string to a program with `<<<`

```bash
$ wc <<< "hello bash"
      1       2      11
```

HERE-DOCUMENT: pass a document with `<<`

```bash
$ wc <<< "hello bash"
      1       2      11
$ wc << wait_for_this
> blah
> blah
> blah
> wait_for_this
      3       3      15
```


# get exit code of last executed program

```bash
$ ls
$ echo $?
0
$ ls foo
ls: foo: No such file or directory
$ echo $?
1
```

# export

variables created with `export` are passed on to all processes created by bash

```
export FOO=BAR
gnome-terminal
```

is equivalent to 

`FOO=BAR gnome-terminal`

# find

`-depth` only enables depth first search and doesn't accept values

global options like `-depth` must always precede filename paths


to search till a particular depth use `-maxdepth` and `-mindepth` instead

```
find . -maxdepth 3 -mindepth 2 foobar.txt
```

# printf
```
$ printf "%02.1f" "12.34"
12.3
```

```
$ printf %06d 123
000123
```
# expr

takes 3 args

```
$ expr 1 + 2
3
$ expr "1" + 3
4
$ expr "1" "+" "4"
5
```

```
$ a=$(expr 1 + 2)
$ echo $a
3
$ expr $a + 1       
4
$ expr "2$a" + 1
24
```

# if else

```bash
#!/bin/bash

if [ "$(uname -s)" = "Darwin" ]; then
	platform="Mac"
else
	platform="Linux"
fi

echo "Platform is $platform"

```

oneliners

```bash
$ if [ "1" = "1" ]; then echo yes; else echo no; fi;
yes

$ if [ "1" = "2" ]; then echo yes; else echo no; fi;
no
```
# input/output/error redirection


https://man7.org/linux/man-pages/man3/stdout.3.html

Under normal circumstances every UNIX program has three streams opened for it when it starts up, one for input, one for output, and one for printing diagnostic or error messages.

`0` => `stdin`

`1` => `stdout`

`2` => `stderr`

`M>&N redirects the output of channel M to channel N.`

`2>&1` => redirecting stderr to stdout

`1>&2` => redirecting stdout to stderr

`2>/path/to/logfile` => redirect stderr to log file

`1>/path/to/logfile` => redirect stdout to log file

# chown

`sudo chown username /path/to/file`
