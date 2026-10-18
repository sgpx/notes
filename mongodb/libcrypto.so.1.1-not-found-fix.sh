#!/bin/bash
platform=$(uname -i)
chksum="c5ac01e760ee6ff0dab61d6b2bbd30146724d063eb322180c6f18a6f74e4b6aa"

apt update
apt install -y build-essential

wget https://www.openssl.org/source/openssl-1.1.1s.tar.gz -O o.tgz
calcsum="$(shasum -a 256 o.tgz | sed -r 's/([a-z0-9]+).+/\1/')"

if [ "$chksum" = "$calcsum" ]; then
	echo checksum match OK
else
	echo checksum match failed, exiting..
	exit 1
fi

tar xvzf o.tgz
cd openssl-1.1.1s
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
