mod mymodule;

fn main() {
	let a = 5;
	let b = crate::mymodule::mymodule::double_this(a);
	println!("{b}");
}
