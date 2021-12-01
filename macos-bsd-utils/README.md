# wildcard escaping 

```
find . -iname *.apk
```

in GNU find is equivalent to

```
find . -iname \*.apk
```

from manpage
```
The special characters used by find are also special characters to many shell programs.  In particular, the characters
     ``*'', ``['', ``]'', ``?'', ``('', ``)'', ``!'', ``\'' and ``;'' may have to be escaped from the shell.
```

# unalias

delete a set alias

```sh
alias cdate="echo $(date +%d-%m-%y)"
alias
unalias cdate
```

# file

check file type and architecture

```
$ cc test.c

$ file a.out
a.out: Mach-O 64-bit executable arm64

$ arch -x86_64 zsh

$ cc test.c

$ file a.out
a.out: Mach-O 64-bit executable x86_64
```
