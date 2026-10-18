#!/bin/bash
echo javac -d pkg-output *.java
javac -d pkg-output *.java

cd pkg-output
echo cd pkg-output
 
echo java auto.Lexus
java auto.Lexus

echo java auto/Lexus
java auto/Lexus
