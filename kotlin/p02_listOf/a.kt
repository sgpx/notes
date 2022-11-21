fun avg( x: List<Int>) : Double
{
	var s : Double = 0.0;
	for(i in x)
	{
		s += i;
	}
	return s/x.size
}

fun main()
{
	val x = listOf<Int>(1,2,3,4,5);
	println(avg(x))	
}
