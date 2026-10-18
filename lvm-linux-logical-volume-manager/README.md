# LVM

logical volume manager

LVM volumes CANNOT be resized while mounted and booted from, need to be attached to different machine or VM

# /dev/mapper

# extend volume size

```
lvextend /dev/mapper/centos-root -L +10G
resize2fs /dev/mapper/centos-root
```

# reduce volume size

```
lvreduce /dev/mapper/centos-root -L -10G
resize2fs /dev/mapper/centos-root
```

# vgscan

https://linux.die.net/man/8/vgscan

scans all disks for volume groups

# lvscan

https://linux.die.net/man/8/lvscan

`sudo lvscan`

