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
