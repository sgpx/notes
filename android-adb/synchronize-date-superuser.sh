#!/bin/bash
# xyz=$(date +%m%d%H%M%Y.%S)
xyz=$(date +"%Y-%m-%d %H:%M:%S")
echo "host date is $xyz"
adb shell "echo setting $xyz as AVD date && su root date \"$xyz\""
echo "AVD date is $(adb shell date +\"%Y-%m-%d %H:%M:%S\")"
