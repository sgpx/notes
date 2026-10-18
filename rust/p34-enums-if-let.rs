enum Blah {
	B1(i32),
	B2(i32, i32),
	B3
}


fn main() {
	let a = Blah::B2(5,6);
	if let Blah::B1(x) = a {
		println!("b1 is {x}");
	}
	else if let Blah::B2(x,y) = a {
		println!("b2 {x} {y}");
	}
	else {
		println!("b3");
	}
}

