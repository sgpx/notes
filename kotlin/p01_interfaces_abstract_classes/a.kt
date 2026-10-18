interface inf {
	var foo : Int
	fun bar() : String
	fun baz() {
		println("baz $foo")
	}
}

abstract class newInf constructor (var foo1 :  Int, var foo2 : Int) : inf
{
	init
	{
		this.foo = foo1;
	}
	override fun bar() : String
	{
		println("newbar does not return str")
		return "newbar"
	}
	override fun baz()
	{
		println("newbaz")
	}
	
}

class xInf constructor(var xFoo: Int) : newInf(foo1 = xFoo, foo2 = xFoo)
{
	override var foo : Int = 123;
	init
	{
		this.foo = xFoo;
	}	

	override fun bar(): String
	{
		return "foo is $foo"
	}

	override fun baz()
	{
		println("xbaz")
	}
}

fun main()
{
	val xyz : xInf = xInf(xFoo = 5)
	println(xyz.bar());
	xyz.baz();
}
