#!/bin/bash
qemu-system-x86_64 -cdrom ~/slax-64bit-11.4.0.iso -drive file=target.qcow2,format=qcow2,if=virtio -m 1G -boot d -enable-kvm
