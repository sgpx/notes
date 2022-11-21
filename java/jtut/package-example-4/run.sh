#!/bin/bash
javac auto/automobile/Lexus.java
jar cf x.jar auto/automobile/Lexus.class
javac runit.java
java runit -cp x.jar
cd ..
./xclean.sh
