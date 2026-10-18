import { StatusBar } from "expo-status-bar";
import React from "react";
import { StyleSheet, Text, Button, View } from "react-native";
import AWS from "aws-sdk";
import myCredentials from "./env";
export default function App() {
  const [state, setState] = React.useState([]);
  React.useEffect(() => {}, []);
  const fetchTableData = () => {
    console.log(myCredentials);
    AWS.config.update({
      region: "ap-south-1",
      credentials: myCredentials,
    });
    const db = new AWS.DynamoDB();
    db.listTables((err, data) => {
      console.log(err, data);
      if (!err) {
        setState(data.TableNames);
      }
    });
  };

  return (
    <View style={styles.container}>
      <Button onPress={fetchTableData} title="start"></Button>
      <Text style={{color: "red"}}>List of Tables</Text>
      {state.map((x) => (
        <Text key={x}>{x}</Text>
      ))}
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
