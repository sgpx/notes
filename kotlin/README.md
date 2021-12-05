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

# ~~kotlin interactive shell  : `ki`~~ (DON'T USE, use `kotlin` REPL instead)

## setup (macOS)

`brew install ki`
