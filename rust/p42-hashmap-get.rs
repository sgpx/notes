use std::collections::HashMap;

fn main(){
	let mut a = HashMap::new();
	a.insert("abc".to_string(), 10);
	let x = "abc";
	let y = a.get(x).expect("err");
	println!("y is {}", y);

	let x = "abcd";
	let y = a.get(x).expect("err");

	println!("y is {}", y);
}
