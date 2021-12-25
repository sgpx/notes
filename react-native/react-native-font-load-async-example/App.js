import * as ExpoFonts from "expo-font";
import AppLoading from "expo-app-loading";
import { StatusBar } from "expo-status-bar";
import React from "react";
import { Button, StyleSheet, Text, View } from "react-native";

const MyComponent = ({ value }) => {
  const myRef = React.useRef(99);
  if (value % 3 === 0) {
    myRef.current = myRef.current + 1;
  }
  return (
    <View>
      <Text style={{fontFamily: "comic-sans"}}>value: {value}</Text>
      <Text style={{fontFamily: "comic-sans"}}>survives re-renders: {myRef.current}</Text>
    </View>
  );
};

export default function App() {
  const [loaded, setLoaded] = React.useState(false);
  const [state, setState] = React.useState(0);

  if (loaded === false) {
    return (
      <AppLoading
        startAsync={() => {
          return ExpoFonts.loadAsync({
            "comic-sans": require("./assets/comic-sans.ttf"),
          });
        }}
        onFinish={() => setLoaded(true)}
        onError={() => {}}
      />
    );
  }

  return (
    <View style={styles.container}>
      <Button title="+" onPress={() => setState(state + 1)} />
      <Button title="-" onPress={() => setState(state - 1)} />
      <MyComponent value={state} />
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
  },
});
