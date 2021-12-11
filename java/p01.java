class MyClass
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
