#!/bin/bash
platform=$(uname -i)
apt install -y build-essential
wget https://www.openssl.org/source/openssl-1.1.1o.tar.gz -O o.tgz
tar xvzf o.tgz
cd openssl-1.1.1o
./Configure linux-$platform
make
make install

src="/usr/local/lib"
dest="/usr/lib/$platform-linux-gnu"

libs=(libssl libcrypto)

for i in {0..1}; do
	fspath="$src/${libs[$i]}.so.1.1";
	fdpath="$dest/${libs[$i]}.so.1.1";
	echo ln -s $fspath $fdpath;
	ln -s $fspath $fdpath;
done
