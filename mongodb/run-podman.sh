#!/bin/bash
dl_link_aarch64="https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-ubuntu2004-5.0.6.tgz"
dl_link_x86_64="https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-5.0.6.tgz"

arch=$(uname -i)
echo arch is $arch

if [ "$arch" = "aarch64" ]; then
	dl_link="$dl_link_aarch64"
else
	dl_link="$dl_link_x86_64"
fi

if [ ! -r mdb ]; then
	apt update
	apt install -y curl wget
	wget -v $dl_link
	mv -v *.tgz m.tgz
	mkdir xtmp
	tar xvzf m.tgz -C xtmp
	mv -v xtmp/* mdb
	rmdir xtmp
fi

opt=""
dbdata_path=~/dbdata
nx=""

function set_opt(){
	opt="--auth"
}

function clear_dbdata(){
	rm -rf $dbdata_path
	mkdir $dbdata_path
}

function set_nohup(){
	nx="nohup"
}

function process_arg(){
	if [ "$1" = "a" ]; then
		echo setting opt
		set_opt;
	fi

	if [ "$1" = "r" ]; then
		echo clearing dbdata
		clear_dbdata;
	fi

	if [ "$1" = "n" ]; then
		echo setting nohup;
		set_nohup;
	fi

}

arg="$1"
arg_len=${#arg}
ctr=0

while (( $ctr < $arg_len )); do process_arg "${arg:$ctr:1}"; ctr=$(expr $ctr + 1); done

cd mdb/bin
pwd
cmd="$nx ./mongod --bind_ip 0.0.0.0 --port 5000 --dbpath $dbdata_path $opt &"
echo $cmd
$cmd
