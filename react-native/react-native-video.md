# install

expo managed projects must be ejected

`react-native install react-native-video@https://github.com/matrixfrog/react-native-video`

```
import { Button, StyleSheet, Text, View, Image } from "react-native";
import React from "react";
import Video from "react-native-video";

export default function App() {
  return (
    <View
      style={{
        flex: 1,
        width: "100%",
        height: "100%",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Video</Text>
      <Video
        paused={false}
        repeat={true}
        source={{ uri: "https://example.com/foo.mp4" }}
        style={{ width: 500, height: 300 }}
        resizeMode="stretch"
      />
    </View>
  );
}
```
