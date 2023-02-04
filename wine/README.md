# wine

# install

`sudo apt install -y wine`

winetricks

`sudo apt install -y winetricks`

ntlm_auth

`sudo apt install -y winbind`

# environment

set WINEPREFIX

`export WINEPREFIX=/home/ubuntu/wineroot`

# set wine configuration

change OS and settings with winecfg

`winecfg`

`WINEPREFIX=$wineroot winecfg`

# run program

`wine a.exe`

# debug program

`winedbg a.exe`

# run windows built-in programs

command prompt

`wine cmd.exe`

explorer

`wine explorer.exe`

control panel

`wine control.exe`
