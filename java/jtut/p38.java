class superclass {
	int num = 20;
	superclass(int x)
	{
		this.num = x;
	}
	public void display()
	{
		System.out.println("Number is "+num);
	}
}

class su2 extends superclass {
	int num = 10;
	public void m(){
		this.display();
	}
}

class p38 {
	public static void main(String[] args){
		su2 p = new su2(10);
		System.out.println(p.num);
	}
}
