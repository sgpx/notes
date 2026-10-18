data class Coordinate(val x : Double, val y : Double, val pointName : String){
	val dist : Double = Math.sqrt((x*x) + (y*y));
}

fun main(){
	val p1 = Coordinate(5.0,6.0,"p1");
	println("${p1.x} ${p1.y} ${p1.dist}");
}
