class abc {
	abc()
	{
		System.out.println("created abc");
	}
	protected void finalize()
	{
		System.out.println(123);
	}
}
class p33 {
	public static void main(String[] args){
		abc foo = new abc();
	}
}
