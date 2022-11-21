#!/bin/bash
username="foobar"
apt update
apt install -y sudo nano
useradd $username
visudo
