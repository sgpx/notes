#!/bin/bash

platform=$(uname -p)

if [ "$platform" = "arm" ]; then
	url="https://fastdl.mongodb.org/osx/mongodb-macos-arm64-6.0.3.tgz"
else
	url="https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.3.tgz"
fi

if [ ! -r mongodb.tgz ]; then
	curl -v -L $url -o mongodb.tgz
fi

tar xvzf mongodb.tgz
mv -v mongodb-*/ mdb/ 
cd mdb/bin
pwd
mkdir dbdata
./mongod --bind_ip 0.0.0.0 --dbpath dbdata --port 5000


