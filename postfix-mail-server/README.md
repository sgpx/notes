# setup (ubuntu)

`sudo apt install -y postfix`

# log path

`/var/log/mail.log`

`grep postfix /var/log/syslog`

# error log

`/var/log/mail.err`

# force ipv4/ipv6

edit inet_protocols in post

`sed -i /etc/postfix/main.cf -r "s/^inet_protocols = all$/inet_protocols = ipv4/"`

# ref

http://www.postfix.org/postconf.5.html
