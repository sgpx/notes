#!/bin/bash
source ~/activate-maven.sh
mvn archetype:generate -DgroupId="com.example"  -DartifactId="myProject" -DarchetypeArtifactId="maven-archetype-quickstart" -DinteractiveMode="false"
