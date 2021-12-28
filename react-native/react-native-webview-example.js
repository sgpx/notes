import { StatusBar } from "expo-status-bar";
import { Dimensions, StyleSheet, Button, View } from "react-native";
import WebView from "react-native-webview";
import React from "react";

export default function App() {
  const [state, setState] = React.useState("https://reactnative.dev");
  return (
    <View style={styles.container}>
      <Button title="123" onPress={() => setState("https://reactjs.org/")} />
      <WebView
        style={{
          width: Dimensions.get("window").width,
          height: "50%",
          borderColor: "black",
          borderWidth: 2,
        }}
        source={{ uri: state }}
      />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    paddingTop: 50,
  },
});
