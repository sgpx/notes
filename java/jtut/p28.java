class p28 {
	public static int foo(int x, int y){
		return x*y;
	}
	public static double foo(double x, double y){
		return x*y;
	}
	public static void main(String[] args){
		int a = foo(5,6);
		double b = foo(5.5,6.6);
		System.out.println(a);
		System.out.println(b);
	}
}
