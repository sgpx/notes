#!/bin/bash

if [ ! -d imageoutput/ ]; then
	mkdir imageoutput
fi

fn=$(sed -r "s/.pdf//" <<< $1)
tf="$fn.jpg"
convert -verbose -density 300 -quality 100 $1 $tf
echo convert -verbose -append $(ls $fn-*.jpg) $tf
convert -verbose -append $(ls $fn-*.jpg) $tf
mv -v $tf imageoutput/$tf
rm -v *.jpg
