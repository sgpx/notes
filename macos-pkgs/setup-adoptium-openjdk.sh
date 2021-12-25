#!/bin/bash
download_link="https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.13%2B8/OpenJDK11U-jdk_x64_mac_hotspot_11.0.13_8.pkg"
curl -vL $download_link --output temurin11.pkg
xar -xf temurin11.pkg -C temurin11_x64
cd temurin11_x64/net.temurin.11.jdk.pkg
./Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -version
