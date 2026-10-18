# tigervnc

# install server (ubuntu)

`sudo apt install -y tigervnc-standalone-server`

# install client (macOS)

`brew install tigervnc-viewer`

# start server

`tigervncserver :0 -rfbport 1234 -localhost no -geometry 1024x768`

# stop server

`tigervncserver -kill :0`

# list servers

`tigervncserver -list`

# generate passwd file

`vncpasswd -f <<< "lol" > a.txt`

`echo 123 | vncpasswd -f > a.txt`
