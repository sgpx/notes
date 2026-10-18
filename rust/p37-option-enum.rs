use std::io;

fn odd_only(x : i32) -> Option<i32> {
	if x % 2 == 1 { return Some(x); }
	else { return None; }
}

fn main() {
	let mut istr = String::new();
	io::stdin().read_line(&mut istr).expect("readline error");
	let i : i32 =  istr.trim().parse().expect("parse error");
	let a = odd_only(i);

	if let Some(b) = a {
		println!("a is odd, Some(b) : {b}");
	}
	else {
		println!("a is even");
	}
}
