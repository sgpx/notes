import { StatusBar } from "expo-status-bar";
import React, { useRef, useState } from "react";
import { FlatList, StyleSheet, Text, View } from "react-native";

export default function App() {
  const flatListRef = useRef(null);
  const xarr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const [state, setState] = useState(xarr);

  const handleScroll = (event) => {
    const { layoutMeasurement, contentOffset, contentSize } = event.nativeEvent;
    const isCloseToBottom =
      layoutMeasurement.height + contentOffset.y >= contentSize.height - 20; 

    if (isCloseToBottom) {
      console.log("ok");
      const x2 = Array(10)
        .fill(1);
      setState([...state, ...x2]);
      console.log(state.length);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <FlatList
        ref={flatListRef}
        data={state}
        keyExtractor={() => parseInt(Math.random() * Math.pow(10, 7))}
        renderItem={(p) => (
          <View
            style={{
              height: 100,
              backgroundColor: "yellow",
              width: 100,
              margin: 10,
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Text>{p.index}</Text>
          </View>
        )}
        onScroll={handleScroll}
        scrollEventThrottle={16}
      ></FlatList>
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
