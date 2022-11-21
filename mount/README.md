# mount

## mount NTFS filesystem (readonly)

`sudo mount -r -t ntfs-3g /dev/my-ntfs-partition my-mount-point`

## mount 9PFS share

`sudo mount -t 9p -o trans=virtio $host_id /mnt/9pshare -oversion=9p2000.L`
