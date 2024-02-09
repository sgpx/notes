#!/bin/bash
libraries=(ssl crypto)
for l in ${libraries[@]}; do
	echo copying $i; 
	for i in $(find /opt/homebrew/opt/openssl\@3/lib -name "lib${l}*"); do
		echo cp -v $i /opt/homebrew/opt/libpq/lib/;
		cp -v $i /opt/homebrew/opt/libpq/lib/;
	done; 
done

echo "[press any key to delete when build is done]"
read

for i in ${libraries[@]}; do
	echo removing /opt/homebrew/opt/libpq/lib/lib$i*
	rm -vf /opt/homebrew/opt/libpq/lib/lib$i*
done
