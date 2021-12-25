# TURTLE CLI

build expo apps offline

# get distribution key for iOS

`expo fetch:ios:certs`

# build for ios simulator

```bash
#!/bin/bash
export EXPO_USERNAME="expo-io-username"
export EXPO_PASSWORD="expo-io-password"
export EXPO_IOS_DIST_P12_PASSWORD="$(expo fetch:ios:certs | grep Distribution | sed -r 's/.+\: (.+)/\1/')"
export TEAM_ID="my-team-id"
turtle bi --dist-p12-path ./x.p12  --provisioning-profile-path ./x.mobileprovision --team-id $TEAM_ID --type simulator
```

# view expo hosted manifest from exp.host

```bash
curl -v -H "Exponent-SDK-Version: 43.0.0" -H "Exponent-Platform : ios"  https://exp.host/@my-expo-io-username/my-project | jq '.';
```
