#!/bin/bash
sudo rm /tmp/.X0-lock /tmp/.X11-unix/X0 
export DISPLAY="$(hostname):0"
vncserver -kill :0
vncserver :0
sudo cp -v ~/.Xauthority /root
fvwm &
