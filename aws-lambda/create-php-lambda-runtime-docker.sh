#!/bin/bash
docker run --name a1 -d -it amazonlinux:2023 bash
echo 'build_path="/root/pbuild"
mkdir $build_path
dnf update
yes | dnf install re2c bison autoconf make libtool libxml2-devel sqlite-devel git zip
git clone --depth 1 https://github.com/php/php-src
cd php-src
nohup ./buildconf
nohup ./configure --prefix=$build_path
nohup make -j5
nohup make install
cd $build_path
mv /root/bootstrap .
chmod +x bootstrap
zip -r /root/php-runtime.zip .' > tmp.sh
docker cp custom-runtime-tutorial/bootstrap a1:/root/bootstrap
docker cp tmp.sh a1:/root/run.sh
rm tmp.sh
docker exec a1 /bin/bash /root/run.sh
docker cp a1:/root/php-runtime.zip .
