#!/bin/bash
target="~/.local/share/containers/podman/machine/qemu/podman-machine-default_fedora-coreos-36.20221030.2.3-qemu.aarch64.qcow2"
qemu-system-x86_64 -cdrom ~/slax-64bit-11.4.0.iso -drive file=$target,format=qcow2,if=virtio -m 1G -boot d -virtfs local,path=~/sharepath,mount_tag=$host_id,security_model=none,id=$host_id

printf "to access local shared path use:\n'mount -t 9pfs -o trans=virtio $host_id /path/to/mountpoint'"
