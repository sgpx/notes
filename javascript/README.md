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
