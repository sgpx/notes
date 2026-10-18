class abc {
	public int x = 99;
	public abc(int y)
	{
		this.x = y;
		System.out.println("abc");
	}
}

class p30 {
	public static void main(String[] args){
		abc foobar = new abc(7);
		System.out.println(foobar.x);
	}
}
