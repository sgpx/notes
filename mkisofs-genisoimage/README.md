# mkisofs/genisoimage

# ref

iso9660 standard

# example

`mkisofs -o ../my.iso .`

# set el torito boot file

`mkisofs -o ../my.iso -b ./path/to/bootfile .`

# set efi boot file

`mkisofs -o ../my.iso -e efi.img .`

`mkisofs -o ../my.iso -efi-boot efi.img .`
