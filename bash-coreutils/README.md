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


