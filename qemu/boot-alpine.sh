#!/bin/bash
cdboot=0
qcow2_attached=0

isopath="alpine.iso"
qcow2_path="a.qcow2"
opts=""
opt_accel=""

if [ "$(uname -s)" = "Darwin" ]; then
	opt_accel+="-accel tcg"
else
	opt_accel+="-accel kvm"
fi

if [ "$cdboot" = "1" ]; then
	opts+="-boot d -cdrom $isopath"
fi

if [ "$qcow2_attached" = "1" ]; then
	opts+="-drive file=$qcow2_path,format=qcow2,if=virtio"
fi

qemu-system-x86_64 $opts $opt_accel -m 7G -smp cpus=4 -nic user
