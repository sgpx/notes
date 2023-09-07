# vnc

# tightvnc server

`sudo apt install -y tightvncserver fvwm xterm`

# set xinitrc

`sudo echo "fvwm &" > /etc/X11/xinit/xinitrc`

# start

`vncserver :0`

# kill old server

`vncserver -kill :0`

# manually clear lock

`sudo rm /tmp/.X0-lock /tmp/.X11-unix/X0`

# viewer on macOS

`brew install tigervnc-viewer`

# launch applications

```
export DISPLAY=":0"
xterm &
```

```
export DISPLAY="${hostname}:0"
fvwm &
```
# copy xauthority to root to avoid MIT MAGIC COOKIE errors while launching apps as root

`sudo cp .Xauthority /root`
