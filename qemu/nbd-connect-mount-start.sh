#!/bin/bash
#imgpath="/var/lib/libvirt/images/centos6.8.qcow2"; partname="/dev/nbd0p1"
#imgpath="/var/lib/libvirt/images/centos6.8-clone.qcow2"; partname="/dev/nbd0p2"
imgpath="/var/lib/libvirt/images/archlinux.qcow2"; partname="/dev/nbd0p2"

sudo modprobe nbd
sudo qemu-nbd --connect=/dev/nbd0 $imgpath
sudo fdisk -l /dev/nbd0 # get list of filesystems inside image
sudo mount $partname vmdrive
