fun main()
{
    val f1 : (String) -> String = { str : String -> "$str $str" }
    println(f1("hey"))

    val f2 : (String,Int,Double) -> String = { str: String, x : Int, y : Double -> "$str ${x*y}" }
    println(f2("hey",2,2.3))

    val f3 = { str : String, x : Int -> "$str $x" }
    println(f3("hey",123))
}
