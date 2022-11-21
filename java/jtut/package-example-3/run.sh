#!/bin/bash
echo javac auto/automobile/Lexus.java
javac auto/automobile/Lexus.java
echo javac runit.java -cp .
javac runit.java -cp .
echo java runit
java runit

for i in $(find . -iname \*.class -depth); do echo removed $i; rm $i; done
