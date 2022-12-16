#!/bin/bash
function cleanup()
{
	echo cleaning ".$1" files;
	for i in $(find . -iname "*.$1" -depth); do
		echo removing $i;
		rm -v $i;
	done;
}

cleanup jar
cleanup class
cleanup out
cleanup o
cleanup obj
cleanup save
cleanup tgz
cleanup tar.gz
