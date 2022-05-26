#!/bin/bash
if [ "$1" = "-a" ]; then
	xcrun simctl list | grep -i booted
else
	xcrun simctl list | grep -i booted | sed -r "s/.+\((.+)\).+\(.+\)/\1/"
fi
