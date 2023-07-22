# assignment operator returns assigned value

```
> console.log(a = 2)
2
> b = (a = 3)
3
> console.log(b)
3
```

# square bracket assignment (assign keys by variable value)

```
a = "foo";
b = {[a] : "bar"};
console.log(b);
> Object { foo: "bar" }
```

# get arrays entries for an object with Object.entries()

```
> a = { x : 1, y: 2}
{ x: 1, y: 2 }
> Object.entries(a)
[ [ 'x', 1 ], [ 'y', 2 ] ]
> Object.entries(a).filter(x => x[1] == 2)
[ [ 'y', 2 ] ]
```

# check if array contains an item with Array.includes()

alternative to indexOf

```
> const a = [1,2,3,"a"];
undefined
> console.log(a.includes("a"));
true
undefined
> console.log(a.includes(1));
true
undefined
> console.log(a.includes(5));
false
```

does not work with objects

```
> a = [{a1:5}]
[ { a1: 5 } ]
> a.includes({"a1":5})
false
> a.includes({a1:5})
false
```

# convert `<input>` file to base64

```
const targetFile = e.target.files[0];
console.log(targetFile);
const reader = new FileReader();
reader.readAsDataURL(targetFile);
reader.addEventListener("load", () => console.log(reader.result));
```

# set computed property names as key values for object initializer

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names

```
const a = 'xyz';
const b = { [a] : 5 };
console.log(b); // { 'xyz' : 5 }
```

equivalent to doing

```
const b = {}
b[a] = 5;
```

# reduce example

```
> a = (x,y) => x + y;
[Function: a]
> [1,2,3].reduce(a)
6
```
# integer to binary string

```
const a = parseInt(Math.random() * Math.power(10,10));
console.log(a);

const b = a.toString(2);
console.log(b);
```

# integer to hex string

```
const a = parseInt(Math.random() * Math.power(10,30));
console.log(a);

const b = a.toString(16);
console.log(b);
```
