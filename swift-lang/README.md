# swift

# REPL

```
$ swift repl
1> print("hello swift")
hello swift
2> :quit
```

# run

$ swift a.swift

# compile and run

$ swiftc a.swift && ./a

# ref

https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/
# entry point

- code at global scope is entry point
- do not need a main function
- no need for semicolons at end of statement

# constants

`let x : Int = 5`

`let s : String = "foo"`

# variables

`var x : Int = 10`

`var s : String = "foo"`

# string concat

```
let x = 5
let y = "hey" + String(x)
print(y)
```

# string sub

```
let x = 5;
let y = "hey \(x)"
print(y)
```

# multiline strings

multiline string literal end must be on a new line

```
let x = """
hey
"""
```

# array

```
var x : Int = [1,2,3]
let b : [Any] = ["swift", 1]
```

# array append

```
var x : Int = [1,2,3]
x.append(4)
```

# dictionaries

```
var x : [Any:Any] = [:]
var y : [Int : Int] = [5:6, 7:8]
var z : [String : String] = ["a" : "b"]
print(z["a"]!)
```

# force unwrap

```
  1> let z = ["a":"b"]
z: [String : String] = 1 key/value pair {
  [0] = {
    key = "a"
    value = "b"
  }
}
  2> print(z["a"])
Optional("b")
  3> print(z["a"]!)
b
```

# if let optional

```
let z = [
	"a" : "b"
]
if let x = z["c"] { print(x) } else { print("nah") }
```

