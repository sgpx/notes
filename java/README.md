# imports should be classes

```bash
$ wget -v https://repo1.maven.org/maven2/org/apache/commons/commons-math/2.2/commons-math-2.2.jar -O x.jar
$ mkdir tmp && cd tmp
$ jar xf ../x.jar
$ ls org/apache/commons/math/Field.class
```

```
import org.apache.commons.math.Field;
```

classpath linking with `--classpath`

```
javac foo.java -cp x.jar && java foo
```

# `javac`

output compiled classes to folder

`javac Xyz.java -d XyzDir/`

# creating an object from a class

TestProgram.java
```
public class MyClass
{
	public MyClass(int myArg)
	{
		System.out.println(myArg);
	}
	public void myMethod(String s, int n)
	{
		for(int i = 0; i < n; i++)
		{
			System.out.println(s);
		}
	}
}

public class TestProgram
{
	public static void main(String[] args)
	{
		MyClass m1 = new MyClass(123);
		m1.myMethod("hello world",3);
	}
}
```

# package-private classes, no modifier

https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html

If a class has no modifier (the default, also known as package-private), it is visible only within its own package.

# openj9/ibm semeru

`source activate-openj9.sh`

supposedly faster than openjdk/hotspot for IO etc but I didn't see any big performance difference on amd64 (openjdk 11 vs openj9 11). android gradle builds are actually faster on hotspot

# create and run a jar

```
javac -d classes foo.java
jar --create --file foo.jar --main-class Abc -C classes/ foo.class
java -jar foo.jar
```
