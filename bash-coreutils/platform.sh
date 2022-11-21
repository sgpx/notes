#!/bin/bash

if [ "$(uname -s)" = "Darwin" ]; then
	platform="Mac"
else
	platform="Linux"
fi

echo "Platform is $platform"
