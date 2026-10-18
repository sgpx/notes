import { StatusBar } from "expo-status-bar";
import { Button, StyleSheet, Text, View, Image } from "react-native";
import * as ExpoImagePicker from "expo-image-picker";
import React from "react";
import * as ExpoImageManipulator from "expo-image-manipulator";

export default function App() {
  const [state, setState] = React.useState("");
  const fx = async () => {
    await ExpoImagePicker.getMediaLibraryPermissionsAsync();
    const res1 = await ExpoImagePicker.launchImageLibraryAsync({
      mediaTypes: ExpoImagePicker.MediaTypeOptions.Images,
      base64: true,
    });
    if (!res1.cancelled) {
      const extension = res1.uri.split(".").pop();

      const res2 = await ExpoImageManipulator.manipulateAsync(
        res1.uri,
        [{ resize: { height: 300, width: 300 } }],
        { format: "jpeg", base64: true }
      );
      const imageData = res2.base64;
      console.log(imageData);
      const imageBase64 = `data:image/${extension};base64,${imageData}`;
      setState(imageBase64);
    }
  };
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <Button onPress={fx} title="Open" />
      {state ? (
        <Image
          source={{ uri: state }}
          style={{
            width: 300,
            height: 300,
            resizeMode: "contain",
            borderColor: "red",
            borderWidth: 1,
          }}
        />
      ) : (
        <React.Fragment />
      )}
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
