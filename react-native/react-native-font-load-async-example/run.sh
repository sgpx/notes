#!/bin/bash
expo init app1  # blank
cd app1
expo install expo-font expo-app-loading
cp ../App.js .
cp ../comic.ttf ./assets
