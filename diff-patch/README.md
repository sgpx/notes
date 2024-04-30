```
$ ls
a.txt b.txt
$ cat a.txt
foo bar
$ cat b.txt
foo
$ diff a.txt b.txt > x.diff
$ ls
a.txt  b.txt  x.diff
$ cp b.txt b2.txt
$ cat b2.txt 
foo
$ patch -R b2.txt x.diff 
patching file b2.txt
$ cat b2.txt 
foo
bar
```
