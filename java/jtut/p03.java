class Dog {
	String breed;
	int age;
	String color;
	void barking(){
		System.out.println("bark!");
	}
	void hungry()
	{
		System.out.println("hungry!");
	}
	void sleeping()
	{
		System.out.println("zzz");
	}
}

class p03
{
	public static void main(String[] args)
	{
		Dog newdog = new Dog();
		newdog.barking();
		newdog.sleeping();
		newdog.age = 1;
		System.out.println(newdog.age);
	}
}
