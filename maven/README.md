# maven

# setup (ubuntu)

`sudo apt install -y maven`

# cache

usually stored at `~/.m2` or `$HOME/.m2`

contains jars, pom files for dependencies, etc

# pom

project object model

xml file that contains config info about project

```
<project xmlns = "http://maven.apache.org/POM/4.0.0"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://maven.apache.org/POM/4.0.0
   http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>

   <groupId>com.companyname.project-group</groupId>
   <artifactId>project</artifactId>
   <version>1.0</version>
</project>
```

project -> root tag, specifies schema
modelversion -> version of the model used in POM, usually set to 4.0.0 for maven2/3
groupId -> id of project's group
artifactId -> id of project
version -> version of project

`[groupId]:[artifactId]:[version]`

`org.apache.commons:commons-math:2.2`

# effective pom/super pom

all poms inherit from parent or default

base pom is known as super pom

contains default inherited values

to see effective pom:

`mvn help:effective-pom`

# build lifecycle

sequence of phases

1. `prepare-resources`
2. `validate`
3. `compile`
4. `test`
5. `package`
6. `install`
7. `deploy`

# generate project

`mvn archetype:generate` (interactive mode)

or `mvn archetype:generate -DgroupId="com.example"  -DartifactId="myProject" -DarchetypeArtifactId="maven-archetype-quickstart" -DinteractiveMode="false"` (non-interactive/batch mode)

see `generate-project.sh`

# clean

`mvn clean`

# install

`mvn install`

# create jars

`mvn package`

# compile project

`mvn compile`

for debug info use

`mvn compile -X`

# add compiler targets

put in `pom.xml` inside <project /> tags

```
   <properties>
      <maven.compiler.source>11</maven.compiler.source>
      <maven.compiler.target>11</maven.compiler.target>
   </properties>
```

# add dependencies

make <dependencies /> tag inside <project /> tags in `pom.xml`

put inside <dependencies /> tag 

```
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-math</artifactId>
  <version>2.2</version>
</dependency>
```
