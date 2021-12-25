fun main() {
    val a = 3.14
    println(a::class.java.typeName)

    println(a.toString()::class.java.typeName)

    val x = 1 in 5..7
    println(x)

    when (x) {
        true -> println("x was true")
        else -> println("not true")
    }

    for (i in 1..5) {
        println(i)
    }

    val str: String = "123";
    val nullableStr: String? = null;

    println(nullableStr.toString());
    println(nullableStr?.length);

    /*
    val xint = 1;
    println(xint?.length);

    unresolved referene error
     */
    val xany: Any = 1
    println(xany?.toString());
}
