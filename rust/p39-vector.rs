use std::io;

fn main(){
	let mut v = vec![1,2,3];
	v.push(5);
	println!("{}", v[0]);
	println!("{}", v.len());
}
