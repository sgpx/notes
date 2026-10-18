#!/bin/bash
if [ -d .git ]; then 
	rm -rf .git; 
fi
bn=$(basename $PWD)
gxrclone $bn && mv $bn/.git . && rm -rf $bn
