# adb

to see list of devices:

`adb devices -l`

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

# send a file to connected device

`adb push localfile.ext /path/to/remotefile.ext`

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

`Host-System % adb shell "su && date $(date +%m%d%H%M%Y.%S)" `
