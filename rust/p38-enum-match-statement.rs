enum Abc {
	A(u8, u8),
	B(String, u8),
	C
}


fn check(x : Abc) {
	match x {
		Abc::A(a0, a1) => println!("A {a0} {a1}"),
		Abc::B(b0, b1) => println!("B {b0} {b1}"),
		_ => println!("something else")
	}
}

fn main() {
	let x = Abc::A(5,6);
	let y = Abc::B(String::from("foo"), 7);
	let z = Abc::C;

	check(x);
	check(y);
	check(z);
}
