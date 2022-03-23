#!/bin/bash
dl_link="https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-ubuntu2004-5.0.6.tgz"

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

if [ "$1" = "-a" ]; then
	opt="--auth"
fi

if [ "$1" = "-r" ]; then
	rm -rf $dbdata_path
	mkdir $dbdata_path
fi

cd mdb/bin
pwd
echo ./mongod --bind_ip 0.0.0.0 --port 5000 --dbpath $dbdata_path $opt
./mongod --bind_ip 0.0.0.0 --port 5000 --dbpath $dbdata_path $opt
