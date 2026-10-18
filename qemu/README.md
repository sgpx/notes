# qemu

## fullscreen toggle shortcut

`Ctrl` + `Alt` + `F`

## installation

`sudo apt install -y qemu-system`

## boot using ISO

`qemu-system-x86_64 -cdrom alpine.iso`

## enable KVM	

`qemu-system-x86_64 -enable-kvm -cdrom alpine.iso`

alternatively

`qemu-system-x86_64 -accel kvm -cdrom slax.iso`

## use VNC display

`qemu-system-x86_64 -accel kvm -cdrom slax.iso -display vnc=$DISPLAYNAME`

```
export DISPLAYNAME=2
qemu-system-x86_64 -accel kvm -cdrom slax.iso -display vnc=":$DISPLAYNAME" &
gvncviewer localhost:$DISPLAYNAME
```

# qcow2

qemu copy on write disk image format

## create

`qemu-img create example.qcow2 10G # creates raw image`

`qemu-img create -f qcow2 /var/lib/libvirt/images/disk1.img 100M`

`qemu-img create -f qcow2 /var/lib/libvirt/images/disk1.img 1G`

## convert images

`qemu-img convert -f raw -O qcow2 raw.img foo.qcow`

# qemu-nbd

qemu network block device server

## setup

```
sudo apt install -y qemu-utils libnbd
sudo modprobe nbd
```

## connect to QCOW2 image

```
sudo qemu-nbd --connect=/dev/nbd0 foo.qcow2
sudo fdisk -l /dev/nbd0 # get list of filesystems inside image
sudo mount -r /dev/nbd0p3 /mnt/point
``` 

## disconnect QCOW2 nbd

```
sudo umount /mnt/point
sudo qemu-nbd --disconnect /dev/nbd0
```

# ref

https://wiki.gentoo.org/wiki/QEMU/Options
