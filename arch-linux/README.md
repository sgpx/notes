# arch linux

## installing

## mount /proc

`mount -t proc none /proc`

## chroot issues

`/etc/mtab/` points to `../proc/self/mounts`

## chroot DNS resolution issues

DNS resolution is usually provided by `systemd-resolved`

`echo nameserver 127.0.0.53 > /etc/resolv.conf`

# install gnome

```
pacman -S gnome-shell gnome-terminal wayland
gnome-shell --wayland
```

# cloudimg

see cloud-init https://cloudinit.readthedocs.io/en/latest/tutorial/qemu.html and follow steps to make user-data vendor-data etc

login to the cloud image with username arch and password `password`

```
#!/bin/bash
imgpath=./arch.qcow2
isopath=/home/myuser/edrive/tmp/ubuntu-22.04.4-desktop-amd64.iso

#sudo qemu-system-x86_64 -cdrom $isopath -accel kvm -vga std -drive file=$imgpath,format=qcow2,if=virtio -vga std -boot d -m 9G -smp cpus=2
sudo qemu-system-x86_64 -accel kvm -vga std -drive file=$imgpath,format=qcow2,if=virtio -vga std -boot d -m 9G -smp cpus=2 -smbios type=1,serial=ds='nocloud;s=http://10.0.2.2:8000/'
```
