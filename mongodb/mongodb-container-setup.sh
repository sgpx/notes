#!/bin/bash

download_link="https://fastdl.mongodb.org/linux/mongodb-linux-aarch64-ubuntu2004-5.0.5.tgz"

fn=$(sed -r "s/^(.+)\/(.+)/\2/" <<< $download_link)
apt update
apt install -y wget curl
wget -v $download_link
tar xvzf $fn
mv -v $fn/ mdb/
cd mdb/bin
ls

