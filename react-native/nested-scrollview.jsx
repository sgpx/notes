import React from "react";
import { View, Text, TouchableOpacity, ScrollView, Image } from "react-native";

const Xyz = () => (
  <ScrollView
    horizontal={true}
    style={{ , width: "100%", height: 100, backgroundColor: "blue" }}
    contentContainerStyle={{
      justifyContent: "center",
      alignItems: "center",
      backgroundColor: "green",
      flexGrow: 1,
    }}
	nestedScrollEnabled={true}
  >
    <View
      style={{ backgroundColor: "red", width: 100, height: 50, margin: 10 }}
    ></View>
    <View
      style={{ backgroundColor: "red", width: 100, height: 50, margin: 10 }}
    ></View>
    <View
      style={{ backgroundColor: "red", width: 100, height: 50, margin: 10 }}
    ></View>
    <View
      style={{ backgroundColor: "red", width: 100, height: 50, margin: 10 }}
    ></View>
  </ScrollView>
);

export default function HomeScreen(props) {
  return (
    <View style={{flex:1, width:"100%", height: "100%", justifyContent: "flex-start", alignItems: "center"}}>
      <ScrollView style={{ width: "100%",  }}>
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
        <Xyz />
      </ScrollView>
      <View style={{height: 100, width: "100%", backgroundColor : "yellow"}}></View>
    </View>
  );
}
