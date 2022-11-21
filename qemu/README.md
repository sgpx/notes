# qemu

## installation

`sudo apt install -y qemu-system`

## boot using ISO

`qemu-system-x86_64 -cdrom alpine.iso`

## enable KVM	

`qemu-system-x86_64 -enable-kvm -cdrom alpine.iso`

# qcow2

qemu copy on write disk image format

## create

`qemu-img create -f qcow2 /var/lib/libvirt/images/disk1.img 100M`

`qemu-img create -f qcow2 /var/lib/libvirt/images/disk1.img 1G`

# qemu-nbd

qemu network block device server

## install

`sudo apt install -y qemu-utils`

## connect to QCOW2 image

```
sudo qemu-nbd --connect=/dev/nbd0 foo.qcow2
sudo fdisk -l /dev/nbd0 # get list of filesystems inside image
sudo mount -r /dev/nbd0p3 /mnt/point
``` 

# ref

https://wiki.gentoo.org/wiki/QEMU/Options
