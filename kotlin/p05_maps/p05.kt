fun main()
{
	val mapOne = mapOf<Int,String>(1 to "foo", 2 to "bar")
	println(mapOne[1])
	// regular maps can't be changed

	val mapTwo = mutableMapOf<Int,String>(1 to "foo")
	mapTwo.put(2,"bar")
	mapTwo.put(3,"baz")

	println(mapOne.toString())
	println(mapTwo.toString())
}
