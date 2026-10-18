#!/bin/bash
qcowpath="/var/lib/libvirt/images/archlinux.qcow2"
isopath="/home/ubuntu/iso/archlinux-jan2023.iso"

qemu-system-x86_64 -cdrom $isopath -drive file=$qcowpath,format=qcow2,if=virtio -m 4G -boot d -accel kvm

