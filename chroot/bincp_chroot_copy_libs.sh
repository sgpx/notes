#!/bin/bash
target="$1"
newroot="$2"
for i in $(ldd $target | grep "=>" | sed -r "s/.+=> (.+) \(.+/\1/" ); do cp -v $i $newroot$i; done
