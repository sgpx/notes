#!/bin/bash
if [ "$2" = "--reset" ]; then
	rm $HOME/.ftpsend
fi

if [ ! -r "$HOME/.ftpsend" ]; then
	echo "enter ip address [192.168.(XXX.XXX):2121]"
	read a;
	ipaddr="192.168.$a:2121"
	echo ip address is $ipaddr
	echo $ipaddr > $HOME/.ftpsend
fi

if [ ! -r $1 ]; then
	echo error: file \"$1\" does not exist
	exit
fi

fn=$(realpath $1)
tfn=$(sed -r "s/^.+\/(.+)$/\1/" <<< $fn)
u=ftp
p=ftp

url="ftp://$u:$p@$(cat ~/.ftpsend)/$tfn"
cmd="curl -v -T $fn $url"
echo $cmd
$cmd
