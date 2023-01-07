# example

ref : https://www.cyberciti.biz/faq/unix-linux-chroot-command-examples-usage-syntax/

```
mkdir newroot
cd newroot
mkdir bin lib lib64
cp ~/busybox bin
sudo chroot . /bin/busybox sh
```

# bincp : copy files to new root with attached libs (requires ldd)

```
mkdir newroot
mkdir newroot/bin
bincp /bin/bash $(realpath newroot)
```
