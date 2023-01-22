# weston

reference wayland compositor with integrated terminal and desktop shell

# installation (arch)

`pacman -S weston`

# running

`weston`

`weston --backend=drm-backend.so`

`weston --backend=wayland-backend.so --width=1366 --height=768 # requires parent wayland compositor`

`weston --backend=wayland-backend.so --width=1366 --height=768 --xwayland # requires parent wayland compositor`

# config file

`$HOME/.config/weston.ini`

```
[shell]
background-image=/home/arch/wallpaper.jpg
mode=1366x768
```
