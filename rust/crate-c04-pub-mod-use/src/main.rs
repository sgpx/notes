mod mymodule;
use crate::mymodule::mymodule::double_this as x2;

fn main() {
	let a = 5;
	let b = x2(a);
	println!("{b}");
}
