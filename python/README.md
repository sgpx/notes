# lambdas

no args

```
a = lambda : 123
```

default args

```
a = lambda x=1 : x*2
```

multiple args

```
a = lambda x,y=0 : x+y
```

tuple return

```
a = lambda x: (x,x+1)
```

# DECORATORS

```
@blah
def yada():
	pass
```

is equivalent to

```
yada = blah(yada)
```

```
@app.route("/")
def root():
	return "OK", 200
```

is equivalent to

```
root = lambda : "OK", 200
root = app.route("/")(root)
```

# pad zeroes at start of string

```
>>> "123".zfill(5)
'00123'
```

# convert to binary

str.format()

```
>>> "{0:b}".format(123)
'1111011'
```

bin() function

```
>>> bin(123)
'0b1111011'
```
