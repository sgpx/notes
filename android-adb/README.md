# adb

to see list of devices:

`adb devices -l`

# open logcat/shell for specific device

first, get transport ID of device

```
$ adb devices -l
List of devices attached
emulator-5554          device product:sdk_gphone64_arm64 model:sdk_gphone64_arm64 device:emulator64_arm64 transport_id:4
emulator-5555          device product:sdk_gphone64_arm64 model:sdk_gphone64_arm64 device:emulator64_arm64 transport_id:5
```

```
adb -t 5 logcat
adb -t 4 shell
```

# wipe AVD data

```
emulator -avd Pixel5 -wipe-data
```

# to launch shell for connected device

`adb shell` 

# adb shell - `am` - activity manager

launch app

`am start com.my.app`

# adb shell - `pm` - package manager

install app

`pm install /path/to/my.apk`

uninstall app

`pm uninstall com.my.app`

# logs - `logcat`

`adb logcat | grep ReactNative`

# logcat filter

```
filterspecs are a series of 
  <tag>[:priority]

where <tag> is a log component tag (or * for all) and priority is:
  V    Verbose (default for <tag>)
  D    Debug (default for '*')
  I    Info
  W    Warn
  E    Error
  F    Fatal
  S    Silent (suppress all output)
```

`adb logcat *:E` only shows errors

# send a file to connected device

`adb push localfile.ext /path/to/remotefile.ext`

# get file from connected device

`adb pull /path/to/remotefile.exe localcopy.ext`

# get superuser (to deal with "Operation not permitted" etc errors)

`su`

# run command as superuser

`su root env`
`su root date $HOST_DATE # synchronize date`
`adb shell su root env`

```
Host-System % adb shell "su root env | grep USER"
USER=root
```

# set device date (to prevent date drift errors with TLS etc)

`Host-System % adb shell "su root date $(date +%m%d%H%M%Y.%S)" `

# insufficient permissions error

https://itsfoss.com/fix-error-insufficient-permissions-device/

# adb shell binary

toybox for aarch64

https://landley.net/toybox/about.html

# adb shell netstat and ifconfig

`adb shell ifconfig wlan0`

`adb shell netstat -tlpn`
