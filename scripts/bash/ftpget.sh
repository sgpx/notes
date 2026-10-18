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

fn=$1
u=ftp
p=ftp

url="ftp://$u:$p@$(cat ~/.ftpsend)/$fn"
cmd="curl -v $url -o $HOME/$fn"
echo $cmd
$cmd
