fn main(){
	let mut v = vec![1,2,3];
	v.push(4);
	v.push(5);
	v.push(6);
	let ec = 5;
	let elem_opt = v.get(ec);
	match elem_opt {
		Some(elem_opt) => println!("element {ec} is {elem_opt}"),
		None => println!("element {ec} does not exist")
	}

	for i in &mut v {
		println!("{i}");
	}
}
