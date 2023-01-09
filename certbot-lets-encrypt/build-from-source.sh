#!/bin/bash
# requires c++11 compiler, openssl, rustc and libffi installed
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz -o python.tgz
tar xf python.tgz
cd Python-3.11
./configure --prefix=$python_install --with-openssl=$openssl_install --with-openssl-rpath=$openssl_install/lib
make -j5
make install

export LD_LIBRARY_PATH="$libffi_ld_path:$openssl_install/lib"
export PATH="$PATH:$python_install/bin"

pip3 install certbot
