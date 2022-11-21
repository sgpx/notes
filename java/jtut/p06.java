public class p06 
{
	public String name;
	private int number;

	public int getNumber()
	{
		return number;
	}

	public void setNumber(int x)
	{
		number = x;
	}

	public p06(String nx)
	{
		name = nx;
	}
	public void eprint()
	{
		System.out.println(name+" : "+number);
	}

	public static void main(String[] args)
	{
		p06 lol = new p06("lol");
		lol.setNumber(5);
		System.out.println(lol.getNumber());
		lol.eprint();
	}
}
