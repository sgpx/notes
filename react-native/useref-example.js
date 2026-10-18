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
      <Text>value: {value}</Text>
      <Text>survives re-renders: {myRef.current}</Text>
    </View>
  );
};

export default function App() {
  const [state, setState] = React.useState(0);
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
