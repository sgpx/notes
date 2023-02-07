# arch linux

## installing

## mount /proc

`mount -t proc none /proc`

## chroot issues

`/etc/mtab/` points to `../proc/self/mounts`

## chroot DNS resolution issues

`echo nameserver 127.0.0.53 > /etc/resolv.conf`
