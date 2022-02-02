# `lsof`

check all open ports used by processes

```
$ lsof -i -P | grep 5000
node      555   gt7   xxx  IPv6 0x999999999999999      0t0  TCP *:5000 (LISTEN)
```

# `file` - get file type

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

```
$ file core.54321
core.5461: ELF 64-bit LSB core file, x86-64, version 1 (SYSV), SVR4-style, from './a.out', real uid: 1000, effective uid: 1000, real gid: 1000, effective gid: 1000, execfn: './a.out', platform: 'x86_64

$ file xyz.out 
xyz.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0f9acf4ab1cdf4783733599d30de2e3cc4179fe5, for GNU/Linux 3.2.0, not stripped

$ file cert9.db 
cert9.db: SQLite 3.x database, last written using SQLite version 3011000
```

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
