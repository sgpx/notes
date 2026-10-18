# mir

display server and wayland compositor

# installing

```
pacman -S glib gtest google-glog uttng-lst boost wayland egl-wayland
git clone https://github.com/mirserver/mir
cd mir
cmake . -DMIR_ENABLE_TESTS=OFF # avoid using wlcs
make -j5
make install
```

# running mir shell

mir shell 

```
LD_LIBRARY_PATH=/usr/local/lib miral-shell --shell-terminal-emulator=/usr/bin/terminator --xwayland-path=/usr/bin/Xwayland
```
