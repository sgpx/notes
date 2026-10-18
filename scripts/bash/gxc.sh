#!/bin/bash

if [ -a gx-exec.sh ]; then
	echo executing gx-exec.sh;
	bash gx-exec.sh
fi

if [ -a clean.sh ]; then
	echo executing clean step;
	bash clean.sh;
fi;

cdate=$(date +%Y-%m-%d-%H-%M)

git config user.name sgpx
git config user.email spgithubacc@gmail.com
git config credential.helper store
git add .
git commit -m $cdate
git push
