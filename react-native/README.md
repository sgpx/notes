# touchablewithoutfeedback & scrollview conflict

scrollview wrapped inside
<TouchableWithoutFeedback onPress={Keyboard.dismiss}> </TouchableWithoutFeedback>

will get stuck while scrolling and will only scroll if you tap other scrollable elements

# nested scrollview

nestedScrollEnabled Android
Enables nested scrolling for Android API level 21+.

https://reactnative.dev/docs/scrollview#nestedscrollenabled

# logs

use [`https://www.npmjs.com/package/react-native-logs`](https://www.npmjs.com/package/react-native-logs) for logging to logcat and ios sim process logs

```js
import { logger } from "react-native-logs";

var log = logger.createLogger();

log.debug("This is a Debug log");
log.info("This is an Info log");
log.warn("This is a Warning log");
log.error("This is an Error log");
```

# ---

`useRef(1)` stays detached from app and survives render cycles

`<Image>` width and height must be a square and borderRadius must be half of width for it to be perfect circle

`resizeMode="contain"`
`resizeMode="cover"`
`resizeMode="stretch"`

etc

you can nest `<Text>` components into `<Text>` components

`<View>` does not pass styles to children components but `<Text>` does to child `<Text>` components

# avoid

do NOT put a string value to a numerical StyleSheet style property, it might break some componenents. use style validation provided by StyleSheet

# unverified

dont use `<ScrollView>` with `style={{...,flex: 1}}`

parent `<View>` for `<ScrollView>` must have `style={{flex: 1}}`

