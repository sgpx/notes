# virt-manager

virtual machine manager using qemu and libvirt. comes with networking enabled out of the box

# install

`sudo apt install -y virt-manager`

# run (ubuntu)

```
$ libvirtd &
$ sudo su root -c virt-manager &
```
# qemu image store location

`/var/lib/libvirtd/images/xyz.qcow2`
