# expo application services (EAS)

# setup

```
sudo npm i -g eas-cli
eas login
```

# build APK for android

create eas.json with build profile apkonly with `buildType: "apk"`

```json
{
  "build": {
    "apkonly": {
      "android": {
        "buildType": "apk"
      }
    }
  }
}
```

`eas build -p android --profile apkonly`

# fix "package.json was not found" error

folder name should be the same as name of the project listed in package.json
