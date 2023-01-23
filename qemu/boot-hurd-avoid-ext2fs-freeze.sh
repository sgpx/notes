#!/bin/bash
if [ ! -r hurd.qcow2 ]; then
	qemu-img create hurd.qcow2 20G;
fi

qemu-system-x86_64 -cdrom debian-hurd-mini.iso -accel kvm -m 4G -drive file=hurd.qcow2,format=raw &

