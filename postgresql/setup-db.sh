#!/bin/bash
db_link="https://ftp.postgresql.org/pub/source/v16.1/postgresql-16.1.tar.gz"

ipath=$PWD
data_path=$ipath/db/datastore
install_path=$ipath/db/install

rm -rf db
mkdir db

cd db
mkdir install

wget $db_link -O p.tgz
tar xf p.tgz
mv -v postgres* pg_src
cd pg_src
./configure --without-icu --prefix="$install_path"
make -j10
make install

cd ../install/bin/
./pg_ctl -D $data_path init
./pg_ctl -D $data_path start

