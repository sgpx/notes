use crate::a::B;

pub mod a;

fn main() {
	let x = B { bx : 1, by : 2 }; 
	println!("{} {}", x.bx, x.by);
}
