# setup instructions

`apt install -y openjdk-8-jdk` or get jdk v8/v11 from adoptopenjdk/adoptium

download cmdline tools from [https://developers.google.com/](https://developers.google.com/)

add `platform-tools`, `tools/bin`, etc to `$PATH`

# running sdkmanager

```
./sdkmanager --sdk-path=~/sdk-dir "platform-31"
./sdkmanager --sdk-path=~/sdk-dir "emulator"
```

# delete AVD from command line

macOS

`$HOME/Library/Android/sdk/cmdline-tools/latest/bin/avdmanager delete avd --name Nexus7`
