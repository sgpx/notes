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
