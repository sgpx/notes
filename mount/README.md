# mount

## mount /proc

procfs is a special filesystem that holds process info and other system info

`sudo mount -t proc none /proc`

## mount NTFS filesystem (readonly)

`sudo mount -r -t ntfs-3g /dev/my-ntfs-partition my-mount-point`

## mount 9PFS share

`sudo mount -t 9p -o trans=virtio $host_id /mnt/9pshare -oversion=9p2000.L`

## mount an ISO file

`sudo mount -r -t iso9660 slax.iso /mnt/slax`
