# arch linux

## installing

## mount /proc

`mount -t proc none /proc`

## chroot issues

`/etc/mtab/` points to `../proc/self/mounts`

## chroot DNS resolution issues

DNS resolution is usually provided by `systemd-resolved`

`echo nameserver 127.0.0.53 > /etc/resolv.conf`
