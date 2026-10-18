# ch7

# ch7.1

packages: cargo feature that lets you build, test and share crates

crates: tree of modules that produces library of executables

modules: lets you control organization scope privacy of paths

paths: way of naming an item like a struct function or module

# crate

smallest amount of code rust compiler considers at a time

crates contain modules

modules may be defined in other files that get compiled within the crate

crate has two forms:
- binary: compiles to runnable executable, must have a `main()` function
- library: dont compile to executable, define functionality intended to be shared with multiple projects,
crate root: source file that rust compiler starts from

package: set of one or more crates that provides a set of functionality

cargo.toml : describes how to build crates

cargo : package containing binary crate of the command line tool

package : at least one crate total, contain unlimited binary crates but at most only one library crate

```
$ cargo new project1 && ls project1/src
main.rs
```

- src/main.rs => binary crate root
- src/lib.rs => library crate root

# ch7.2

- when compiling a crate, compiler looks for crate root (src/main.rs)
- modules can be declared in crate root file with `mod` keyword (e.g. `mod vegetables`) in `src/garden.rs`. compiler looks for vegetables

1. inline inside the same file if mod is followed by curly braces
2. in the file `src/garden/vegetables.rs`
3. in the file `src/garden/vegetables/mod.rs`








