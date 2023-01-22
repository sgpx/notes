#!/bin/bash
if [ "$(find --version | grep -i gnu)" != "" ]; then
	args="" # GNU find
else
	args="-depth" # BSD find on MacOS
fi

function cleanup()
{
	echo cleaning ".$1" files;
	for i in $(find . -iname "*.$1" $args); do
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
