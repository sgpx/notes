#!/bin/bash
if [[ -r README.md && "1" = "1" ]]; then
	echo 1
fi

if [[ -r README.md && "1" = "2" ]]; then
	echo 2
fi

if [[ -r README.md && "1"="2" ]]; then
	echo 3
fi

