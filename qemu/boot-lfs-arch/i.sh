#!/bin/bash
imagepath=$HOME/lfs/archlinux.qcow2;
isopath=$HOME/iso/archlinux-jan2023.iso;

function check_image(){
	if [[ ! -a $imagepath ]]; then
		echo image does not exist..
	        echo creating qcow image $imagepath;
	        echo qemu-img create -f qcow2 $imagepath 100G;
	        qemu-img create -f qcow2 $imagepath 100G;
	else
		echo image $imagepath exists;
	fi
}

function run_qemu(){
	echo qemu-system-x86_64 -accel kvm -vga std -drive file=$imagepath,format=qcow2,if=virtio -vga std -m 9G -smp cpus=2 $args;
	qemu-system-x86_64 -accel kvm -vga std -drive file=$imagepath,format=qcow2,if=virtio -vga std -m 9G -smp cpus=2 $args;
}

function boot_arch(){
	check_image;
	args="";

	if [ "$1" = "withcdrom" ]; then
		args="-cdrom $isopath -boot d"
	fi;

	run_qemu $args;
}
