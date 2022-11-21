interface xyz {
	public final int x = 5;
	public void z();
}

class c implements xyz {
	public int x = 10;
	public double y = 1.1;
	public void z(){
		System.out.println(x+y);
	}
}

class p39 {
	public static void main(String[] args){
		c c1 = new c();
		c1.z();
	}
}
