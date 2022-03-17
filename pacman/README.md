# pacman

package manager

# install package

`pacman -S git`

# search package

`pacman -Ss git`

# sync package lists and refresh

`pacman -Sy`

# force package db refresh

`pacman -Syy`

# remove package

`pacman -R git`

# download server list

`/etc/pacman.d/mirrorlist`

```
echo 'Server = https://mirror.aarnet.edu.au/pub/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
```
