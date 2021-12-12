# `-depth` in BSD find vs GNU find

```
find . -iname \*.txt  -depth $depthLevel
```

will give you a list of txt files at depth exactly == $depthLevel

```
find . -iname \*.txt  -depth 1 # all text files in current directory
find . -iname \*.txt  -depth 2 # all text files in subdirectories of current directory
find . -iname \*.txt  -depth 3 # etc
```

`-depth` in GNU find only enables depth-first-search and does not accept values. `-depth` must preceed pathnames like

`find . -depth -iname \*.txt`

use `-maxdepth` in GNU find instead 

`find . -maxdepth 2 -iname \*.txt`

# wildcard escaping in zsh

```
find . -iname *.apk
```

in bash/GNU find is equivalent to

```
find . -iname \*.apk
```
in zsh/BSD find

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

# paste

replace newline in files with something else

```
$ paste a.txt
123
456
567
$ paste -s a.txt
123	456	567
$ paste -s -d , a.txt
123,456,567
```
