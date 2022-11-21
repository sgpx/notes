#!/bin/bash
# $HOME/Library/Android/sdk/emulator/emulator -list-avds

if [ "$1" = "-l" ]; then
	$HOME/Library/Android/sdk/emulator/emulator -list-avds
	exit
fi

if [ "$1" = "" ]; then
	$HOME/Library/Android/sdk/emulator/emulator -avd Pixel_XL_API_31
else
	$HOME/Library/Android/sdk/emulator/emulator -avd "$1"
fi


