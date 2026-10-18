class abc {
	public int x = 99;
	public abc(int y)
	{
		this.x = y;
		System.out.println("abc");
	}
	public void print()
	{
		System.out.println("printing " + this.x);
	}
}

class p31 {
	public static void main(String[] args){
		abc foobar = new abc(7);
		foobar.print();
	}
}
