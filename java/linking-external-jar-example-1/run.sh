#!/bin/bash
wget -v https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.2/commons-math-2.2.jar -O x.jar
javac ext.java -cp x.jar
java ext
