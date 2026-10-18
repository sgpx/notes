#!/bin/bash

a=$(cat ../myfiles.txt)
ctr=0

do_job () {
    i=$1
    b=$(sed -r "s/.+myfiles\/.+\/(.+)/\1/" <<< "$i");
    wget -q $i -O $b
    aws s3 cp $b s3://my-internal-assets/tmp/$b
    rm -v $b
    echo $i : $b
}

export -f do_job # Export the function, so it can be picked up by GNU parallel

cat ../myfiles.txt | parallel do_job
