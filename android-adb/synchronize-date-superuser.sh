adb shell "su root date $(date +%m%d%H%M%Y.%S)"
echo date is $(adb shell date)
