# ftp

# open interactive mode

```
$ ftp
```

# open address

```
$ ftp 1.2.3.4 2021
```

# type

```
$ type ascii
$ type binary
```

# change directory

```
$ cd xyz
```

# get items

```
$ get a.out
$ get oldname.out newname.out
```

# get with curl

`curl -vL ftp://user:pwd@1.2.3.4/a.out -o a.out`

# send with curl

`curl -vT a.out ftp://user:pwd@1.2.3.4/a.out`

