#!/bin/bash
qemu-system-x86_64 -drive file=a.qcow2,format=qcow2,if=virtio -accel kvm -m 9G -smp cpus=2 -nic user
