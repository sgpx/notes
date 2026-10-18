#!/bin/bash
cd chksum_testdir
pwd
a="https://www.openssl.org/source/openssl-1.1.1s.tar.gz"
wget $a
wget $a.sha256
chksum=$(shasum --algorithm 256 openssl-1.1.1s.tar.gz | sed -r "s/([a-z0-9]+).+/\1/")

if [ "$chksum" = "$(cat openssl-1.1.1s.tar.gz.sha256)" ]; then
	echo checksum match OK;
else
	echo checksum match fail;
fi

