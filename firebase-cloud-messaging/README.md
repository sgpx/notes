# google-services.json

- dynamic config `app.config.js` w/ `eas secret:push` as shown in [1] fails to work for `eas buil
d`
- checking into VCS as values can be extracted from APK ("the general answer is yes, the google-s
ervices.json is safe to check in to your repo and is something that should be shared among engine
ers on your team. ")

1. https://docs.expo.dev/build-reference/variables/
2. https://stackoverflow.com/a/42750187
3. https://stackoverflow.com/questions/37358340/should-i-add-the-google-services-json-from-fireba
se-to-my-repository
4. https://groups.google.com/g/firebase-talk/c/bamCgTDajkw
