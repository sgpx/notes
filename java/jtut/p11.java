class p11 {
	public static void main(String[] args){
		int[] numbers = {1,2,3,4,5};
		for(int x : numbers)
		{
			if(x == 3)
			{
				continue;
			}
			if(x == 5)
			{
				break;
			}
			System.out.println(x);

		}
	}
}
