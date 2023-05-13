# ch7

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








