# ed - text editor

# commands

`a` : append text (input mode)

`.` : quit input mode

`w (filename)` : write buffer to file name

`q` : quit ed

# example

```
$ ed
a
the quick brown fox jumps over the lazy dog
.
w x.sh
44
q
$ ls
x.sh
```

# ref

https://www.gnu.org/software/ed/manual/ed_manual.html
