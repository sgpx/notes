#!/bin/bash
cd ~
sudo nohup apt update
sudo nohup apt install -y bzip2 wget libgtk-3-dev libasound2-dev python3-pip python3-venv
wget https://ftp.mozilla.org/pub/firefox/releases/129.0.2/linux-x86_64/en-US/firefox-129.0.2.tar.bz2 -O ff.tar.bzip2
tar xf ff.tar.bzip2
mv firefox* ffinst
sudo ln -s ~/ffinst/firefox /usr/bin/firefox

 
wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz -O geckodriver.tgz
sudo tar xf geckodriver.tgz -C /usr/bin

echo testing firefox, press Ctrl + C to exit
cd ~/ffinst
firefox --headless
