class p27 {
	public static void swap(int x, int y){
		int z = x;
		x = y;
		y = z;
	}
	public static void main(String[] args){
		int x = 1;
		int y = 2;
		swap(x,y);
		System.out.println(x);
		System.out.println(y);
	}
}
