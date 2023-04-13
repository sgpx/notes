use crate::garden::vegetables::Asparagus;

pub mod garden;

fn main() {
	let plant = Asparagus { size : 5 };
	println!("{}", plant.size);
}
