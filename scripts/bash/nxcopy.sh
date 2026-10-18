#!/bin/bash

if [ "$1" = "" ] || [ "$2" = "" ]; then echo no src/destination specified; exit; fi

src="$1"
dest="$2"

mkdir $dest
cd $dest

dfl=$(ls ../$src | sed -r "s/^node_modules$//" | sed -r "s/^venv$//" | sed -r "s/^__pycache__$//")
echo $dfl


