class foo {
	public String fstr;
	public foo(String x)
	{
		fstr = x;
	}
}

class p15 {
	public static void main(String[] args){
		foo[] x = { new foo("hello"), new foo("world") };

		System.out.println(x[0].fstr);
		System.out.println(x[1].fstr);
		System.out.println(x.length);
	}
}
