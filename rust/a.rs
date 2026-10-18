fn check(mut x : String) -> String{
	println!("x is {x}");
	x.push_str(" ya");
	x
}

fn main() {
	let a = String::from("hey");
	let a = check(a);
	println!("a is {a}");
}
