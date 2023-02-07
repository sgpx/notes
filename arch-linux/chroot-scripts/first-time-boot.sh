#!/bin/bash
#qemu-system-x86_64 -cdrom archlinux.iso -drive file=a.qcow2,format=qcow2,if=virtio -accel kvm -boot d #-net user
qemu-system-x86_64 -cdrom archlinux.iso -drive file=a.qcow2,format=qcow2,if=virtio -accel kvm -boot d -m 9G -smp cpus=2 -nic user
