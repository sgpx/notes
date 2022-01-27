class abc {
	int x = 5;
	abc()
	{
		x = 3;
	}
	public void print(int a)
	{
		System.out.println("Printing "+x);
	}
	public void func()
	{
		this.print(this.x);
	}
}
class p32 {
	public static void main(String[] args){
		abc foo = new abc();
		foo.func();
	}
}
