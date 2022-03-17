# list drives

`fdisk -l`

# select drive and open fdisk

`fdisk /dev/sda`

# delete partition

```
Command (m for help): d
Partition number (1-4, default 4): 1
```

# create partition

```
Command (m for help): n
$first_sector
$size # example "+5G"
```

# write partition table

```
Command (m for help): w
```

# print partition table

```
Command (m for help): p
```

