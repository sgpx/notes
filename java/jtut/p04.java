class ducky {
	public ducky()
	{
		System.out.println("foo");
	}
	public ducky(String x)
	{
		System.out.println("bar "+x);		
	}
}

class p04
{
	public static void main(String[] args)
	{
		ducky p1 = new ducky();
		ducky p2 = new ducky("quack");
	}
}
