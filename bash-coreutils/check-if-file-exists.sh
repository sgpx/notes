#!/bin/bash
if [ -a README.md ]; then
	echo README.md exists \(-a\)
fi

if [ -r README.md ]; then
	echo README.md exists and is readable \(-r\)
fi
