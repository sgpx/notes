# struct member access is not allowed inside format string

`println!("{x.a} {x.b}");` will fail

`println!("{} {}", x.a, x.b);` will work

# `option<T>` and `None`

```
fn odd_only(x : i32) -> Option<i32> {
	if x % 2 == 1 { Some(x) }
	else { None }
}

fn main() {
	let a = odd_only(5);
	match a {
		Some(i) => println!("odd number : {}");
		None => println!("even number");
	}
}
```

# string slice

```
let s = String::from("hello world");
let len = s.len();
let slice1 : &str = &s[0..3];
let slice2 : &str = &s[..len];
println!("{} {}", slice1, slice2);
```

# options and expect()

if you put .expect() after a function call that creates an Option<T> you get T instead

```
fn main() {
    let a : String = String::from("abc");
    let b : Option<&str> = a.strip_suffix("bc");
    let c : &str = b.expect("error");
    println!("{a} {c}");
}
```

# ownership rules

rust uses move() and drop() functions to move pointers and clear variables

```
    let s1 = String::from("hello");
    let s2 = s1;
    // s1 is invalidated and cannot be used
    // s1 data is moved completely to s2
    println!("{}, world!", s1);
    // throws a borrow error "borrow of moved value"
```


no restriction for integer values
```

	let s1 : i32 = 1;
	let s2 = s1;
	println("{s1} {s2}");
```


https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html

- Each value in Rust has an owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

# block/function expression return value

```   
let x = {
	let y = 5;
        y + 1 // value without semicolon is block return value
};
```

# statements vs expressions

statements perform an action and do not return a value

expressions return a value

# char.to_digit(radix)

can only convert chars to digits in a number system

like for radix=11, 'a'.to_digit(11) works because 'a' represents the base11 digit 'a' = value "10" in base10 notation

0123456789a

similarly {char}.to_digit(radix = {position} + 10) will fail if char's position in the number system isn't less than the radix

# range

`1..5`

`1..=5`

```
let r1 = 1..5;
let r2 = 1..=5;
let g = 5;
let v1 = r1.contains(&g);
let v2 = r2.contains(&g);
print!("{v1} {v2}\n");
```

# homebrew setup (mac OS)

`brew install rust rustfmt rust-analyzer`

# rustup

rust toolchain installer

https://forge.rust-lang.org/infra/other-installation-methods.html

# install

```
wget -v https://static.rust-lang.org/rustup/dist/aarch64-unknown-linux-gnu/rustup-init
chmod +x rustup-init
./rustup-init
```

# hello world

```
fn main(){
	println!("hello world");
}
```

# macro vs function

`println!` is a macro

```
it does things that functions can't do:

- It parses the format string at compile time, and generates type safe code
- It has a variable number of arguments
- It has named arguments ("keyword arguments") 
```

# build from source

```
./configure --prefix=$foo
python3 x.py build
```

# build a project

```
$ ls
Cargo.toml
$ cargo build
```
