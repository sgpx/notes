#!/bin/bash

a=$(get-media-duration.sh $1  | sed -r "s/([0-9]+)\:([0-9]+)\:([0-9]+).+/\1/")
a=$((a*3600))
b=$(get-media-duration.sh $1  | sed -r "s/([0-9]+)\:([0-9]+)\:([0-9]+).+/\2/")
b=$((b*60))
c=$(get-media-duration.sh $1  | sed -r "s/([0-9]+)\:([0-9]+)\:([0-9]+).+/\3/")
echo $((a+b+c))
