#!/bin/bash
imgpath=/var/lib/libvirt/images/archlinux.qcow2
isopath=$HOME/iso/archlinux-jan2023.iso
sudo qemu-system-x86_64 -cdrom $isopath -accel kvm -vga std -drive file=$imgpath,format=qcow2,if=virtio -vga std -boot d -m 9G -smp cpus=2
