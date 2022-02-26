#!/bin/bash
x=$(which adb)
adb kill-server

sudo "$x" start-server
adb shell
