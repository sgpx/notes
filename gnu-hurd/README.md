# GNU HURD

multiserver microkernel OS

https://hurd.gnu.org

# mini iso

https://cdimage.debian.org/cdimage/ports/latest/hurd-i386/mini.iso

https://cdimage.debian.org/cdimage/ports/latest/hurd-i386/20221029/mini.iso

# boot iso

```
qemu-img create -f qcow2 hurd.qcow2 20G
qemu-system-x86_64 -accel kvm -cdrom mini.iso -m 4G -drive file=hurd.qcow2,format=qcow2 -boot d &
# ext2fs module freezes without sufficient ram
```

# mount iso

```
sudo mount -r -t iso9660 mini.iso hurdiso
cp -r hurdiso hurdcopy 
sudo umount hurdiso
```

# mini iso analysis

all directories inside iso

```
$ isoinfo -i ~/iso/debian-hurd-mini.iso -f | grep -E "^.+[^(;1)]$"
/BOOT
/SYSTEM
/BOOT/GRUB
/BOOT/KERNEL
/SYSTEM/LIBRARY
/BOOT/GRUB/FONTS
/BOOT/GRUB/I386_EFI
/BOOT/GRUB/I386_PC
/BOOT/GRUB/LOCALE

/BOOT/GRUB/ROMS
/SYSTEM/LIBRARY/CORESERV
```

/boot/initrd.gz : gzipped ext2 partition containing boot 

```
isoinfo -i ~/iso/debian-hurd-mini.iso -f | grep -i "initrd"
/BOOT/INITRD.GZ;1
```

/boot/kernel/gnumach.gz : gzipped mach kernel ELF binary

```
isoinfo -i ~/iso/debian-hurd-mini.iso -f | grep -i "initrd"
/BOOT/INITRD.GZ;1
```

# fix weird characters in terminal

change $TERM environment variable from mach-gnu-color to xterm-256-color

```
export TERM=xterm-256-color
```

makeshift clear function() to avoid unknown terminal errors

```
function clear(){
	for i in {1..30}; do
		printf "\n";
	done
}

clear
```
