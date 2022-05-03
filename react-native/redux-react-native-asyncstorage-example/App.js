import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { Provider, useDispatch, useSelector } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";
import persistedReducer from "./persistedReducer";
import { persistor, store } from "./reduxStore";

const RootComponent = () => {
  const globalState = useSelector((x) => x);
  const dispatch = useDispatch();
  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <Text>{JSON.stringify(globalState)}</Text>
      <TouchableOpacity
        style={{ backgroundColor: "red" }}
        onPress={() => {
          dispatch({
            type: "change",
            payload: { a: (globalState.a || 0) + 1 },
          });
        }}
      >
        <Text>Increment</Text>
      </TouchableOpacity>
    </View>
  );
};

export default function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <RootComponent />
      </PersistGate>
    </Provider>
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
