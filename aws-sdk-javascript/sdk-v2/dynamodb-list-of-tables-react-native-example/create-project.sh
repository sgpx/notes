#!/bin/bash
time expo init list-of-tables --template blank
cd list-of-tables
cp -v ../App.js .
cp -v ../env.js .
yarn start
