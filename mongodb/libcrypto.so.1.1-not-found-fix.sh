#!/bin/bash

sudo apt install -y build-essential
wget https://www.openssl.org/source/openssl-1.1.1o.tar.gz
tar xvzf https://www.openssl.org/source/openssl-1.1.1o.tar.gz
cd openssl-1.1.1o.tar.gz
make
sudo make install

src="/usr/local/lib"
dest="/usr/lib/x86_64-linux-gnu"

libs=(libssl libcrypto)

for i in {0..1}; do
	fspath="$src/${libs[$i]}.so.1.1";
	fdpath="$dest/${libs[$i]}.so.1.1";
	echo sudo ln -s $fspath $fdpath;
	sudo ln -s $fspath $fdpath;
done
