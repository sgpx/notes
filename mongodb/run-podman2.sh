#!/bin/bash
arch=$(uname -i)
dl_link="https://fastdl.mongodb.org/linux/mongodb-linux-$arch-ubuntu2004-5.0.6.tgz"

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

function set_opt(){
	opt="--auth"
}

function clear_dbdata(){
	rm -rf $dbdata_path
	mkdir $dbdata_path
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
}

arg="$1"
arg_len=${#arg}
ctr=0

while (( $ctr < $arg_len )); do process_arg "${arg:$ctr:1}"; ctr=$(expr $ctr + 1); done

if [ ! -r $dbdata_path ]; then
	mkdir $dbdata_path;
fi

cd mdb/bin
pwd
echo ./mongod --bind_ip 0.0.0.0 --port 5000 --dbpath $dbdata_path $opt
./mongod --bind_ip 0.0.0.0 --port 5000 --dbpath $dbdata_path $opt
