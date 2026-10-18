# losetup

# attach a loop device

`sudo losetup -f efi.img`

# mount the loop device

`sudo mount -r /dev/loop14 /mnt/foobar`

# list all loop devices

`lsblk | grep -E "^loop"`

# detach loop device

`sudo losetup -d /dev/loop14`

# ref

Loop device is a pseudo-device that makes a computer file accessible as a block device

https://en.wikipedia.org/wiki/Loop_device
