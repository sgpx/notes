data class Coordinate(val x : Int, val y : Int);

fun main(){
	val CoordinateArray : Array<Coordinate> = arrayOf<Coordinate>(
		Coordinate(1,2),
		Coordinate(3,4),
	);
	println(CoordinateArray[0]);
	println(CoordinateArray[1]);
	println("size of CoordinateArray is ${CoordinateArray.size}");
}
