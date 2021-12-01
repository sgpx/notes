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
$ java AKt
hello world
```

```
$ kotlin 1.kt
$ ls
_1Kt.class META-INF
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
