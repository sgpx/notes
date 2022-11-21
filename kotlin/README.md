# kotlin

# setup (macOS)

`brew install kotlin`

# kotlin shell

```
$ kotlin
Welcome to Kotlin version 1.6.0 (JRE 17.0.1+0)
Type :help for help, :quit for quit
>>> 
```

# kotlinc the kotlin compiler

outputs java classes with title case names and Kt attached to the end. numerical filenames get a `_` attached at the beginning

```
$ kotlinc a.kt
$ ls
AKt.class META-INF  a.kt
$ kotlin AKt
hello world
$ java AKt
hello world
```

```
$ kotlinc 1.kt
$ ls
_1Kt.class META-INF
```

specify output directory for classes with `-d`

```
$ kotlinc 1.kt -d xyz/
```

`-d` can output JAR files too

```
kotlinc 1.kt -d 1.jar && java -jar 1.jar
```

# example

```
fun main()
{
	println("hello from kotlin")
}
```

```
$ echo "fun main() { println(\"hello from kotlin\") }" > a.kt && kotlinc a.kt -d a.jar && java -jar a.jar;
hello from kotlin
```

# LAMBDAS


Full Typing

```kotlin
val f1 : (String) -> String = { str : String -> "$str $str" }
```

Variable Type Declaration Omitted

```kotlin
val f3 = { str : String, x : Int -> "$str $x" }
```

```
$ kotlin
Welcome to Kotlin version 1.6.0 (JRE 17.0.1+0)
Type :help for help, :quit for quit
>>> val f1 : (String) -> String = { str : String -> "$str $str" }
>>> f1("hey")
res1: kotlin.String = hey hey
>>> println(f1("hey"))
hey hey
>>> val f2 : (String,Int,Double) -> String = { str: String, x : Int, y : Double -> "$str ${x*y}" }
>>> f2("hey",1,2.3)
res4: kotlin.String = hey 2.3
>>> f2("hey",2,2.3)
res5: kotlin.String = hey 4.6
>>> val f3 = { str : String, x : Int -> "$str $x" }
>>> f3("hey",123)
res7: kotlin.String = hey 123
>>> :quit
```

# NOT NULL ASSERTION OPERATOR `!!`

https://www.baeldung.com/kotlin/not-null-assertion

each type in kotlin has a nullable form and a non-nullable form

`!!` forcibly converts a nullable form to non-nullable form

if null is found, it throws a java `NullPointerException`

```
$ kotlin
Welcome to Kotlin version 1.6.0 (JRE 17.0.1+0)
Type :help for help, :quit for quit
>>> var x : String = "abc"
>>> var y : String? = null
>>> var z : String = y!!
java.lang.NullPointerException
>>> z = x!!
error: unresolved reference: z
z = x!!
^

>>> var z : String = x!!
>>> z
res5: kotlin.String = abc
```

## maps

```kotlin
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
```

```
foo
{1=foo, 2=bar}
{1=foo, 2=bar, 3=baz}
```
