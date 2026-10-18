#!/bin/bash
touchpad_id=$(xinput --list | grep -i touchpad | head -n1 | sed -r "s/.+id=([0-9]+).+/1/")
if [ "$touchpad_id" != "" ]; then
	prop_id=$(xinput list-props $touchpad_id | grep -i "disable while typing enabled (" | sed -r "s/.+(([0-9]+)).+/1/")
	for i in $prop_id; do
		echo xinput set-prop $touchpad_id $i 0
		xinput set-prop $touchpad_id $i 0
	done
else
	echo touchpad not found
fi
