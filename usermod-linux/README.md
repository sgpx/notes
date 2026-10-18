# append group to user

`usermod -a -G mygroup myuser`

`usermod --append --groups mygroup myuser`

# change user home directory path

`usermod --home /tmp/newhome myuser`

# change user default shell

`usermod --shell /bin/sh myuser`
