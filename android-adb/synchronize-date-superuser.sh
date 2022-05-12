#!/bin/bash
echo "su root date '$(date +%m%d%H%M%Y.%S)'"
adb shell "su root date $(date +%m%d%H%M%Y.%S)"
adb shell date
