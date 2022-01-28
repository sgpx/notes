package auto;

class Lexus implements Car {
	public void wheels(){
		System.out.println(4);
	}

	public static void main(String[] args)
	{
		Lexus LFA = new Lexus();
		LFA.wheels();
	}
}
