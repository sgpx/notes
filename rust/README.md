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
