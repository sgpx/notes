# addition/subtraction/etc

```
$ a=1
$ b=2
$ c=$((a+b))
$ echo $c
3
$ echo $((5-3))
2
$ echo $((2*33*44))
2904
$ echo $((100/9))
11
$ echo $((8%5))
3
```

# `export`

with an argument it provides the declared variable to all subsequent child processes of the shell

if used without any arguments it will echo list of commands to export environment variables

```
$ export
declare -x HOME="/home/ubuntu"
```

# `test`

utility for checking file types and comparing values

```
$ ls
foo
$ if [ -r foo ]; then echo foo exists; else echo foo doesn't exist; fi
foo exists
$ if test -r foo; then echo foo exists; else echo foo doesn't exist; fi
foo exists
```

# single brackets vs double brackets

brackets are equivalent of coreutils utility `test`

single brackets are POSIX, double brackets are a bash/zsh extension for clearer syntax

# `-a` conditional

in single brackets, evaluates to POSIX boolean expression comparison operator

in bash double brackets, evalutes to `-a : True if file exists` (https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)

# array length

```
foo=$("$@")
echo ${#foo[@]}
```

# args to array

```
foo=("$@")
```

# substring syntax

```
str=foobar
a=1
b=2
len=1

echo ${str:$a:$len}
echo ${str:$b:$len}
```

# string length

```
a=foobar
echo ${#a}
```

# while loop

```
a=1; b=4; while (( $a < $b )); do echo $a; a=$(expr $a + 1); done
```

# NOT operator in conditional expressions (!)

```
if [ ! -r foo.txt ]; then
	echo foo.txt foo doesn't exist
fi
```

# pushd && popd

```bash
$ pwd
/
$ pushd node_modules/event-emitter/benchmark/
/node_modules/event-emitter/benchmark 
$ pwd
/node_modules/event-emitter/benchmark
$ popd
$ pwd
/
```

# date

```bash
$ date +%s
1641556789
$ old_time=$(date +%s)
$ new_time=$(expr "$old_time" "-" "100")
$ date --set="@$new_time"

# get YYYY-MM-DD

$ date +%F
2022-10-23
```

# functions

```bash
#!/bin/bash
function myfunc(){
	echo arg1 is $1
	echo arg2 is $2
	argsum=$(expr "$1" "+" "$2")
	echo "expr '$1' '+' '$2' = $argsum"
}

myfunc 3 4
```

# numerical comparison

```bash
a=1
b=2
if [ $a -eq $b ]; then echo equals; fi
if [ $a -ne $b ]; then echo does not equal; fi
```

# aliases

shorthands for one or more commands

```bash
alias svenv=source venv/bin/activate
svenv
```


```bash
alias ppap="for i in {1..3}; do echo $i; done; ls; pwd;"
```

# semicolon line termination

semicolons must be escaped in bare strings

example: to output `123;` to a file

```
echo 123; > a.txt
```

will output 123 to stdout and create an empty a.txt file because `> a.txt` will pipe stdin to a.txt (in zsh, it will wait for stdin input instead)


use escaped semicolon instead

```
$ echo 123\; > a.txt
$ cat a.txt
123;
```
# version differences in HERE-STRING

test program

```bash
#!/bin/bash
bash --version

test_str="1_2"
IFS="_" read -a tmp <<< $test_str

for i in {0..2};
	do echo tmp$i ${tmp[$i]};
done
```

bash 3.2 output (treats $test_str "1_2" as "1 2") (putting $test_str in quotes as `<<< "$test_str"` solves this problem)
```
$ ./test-bash-here-string.sh 
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin20)
Copyright (C) 2007 Free Software Foundation, Inc.
tmp0 1 2
tmp1
tmp2
```

bash 5.0 output
```
root@41d8cce0e049:/# ./test-bash-here-string.sh
GNU bash, version 5.0.17(1)-release (aarch64-unknown-linux-gnu)
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
tmp0 1
tmp1 2
tmp2
```
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
