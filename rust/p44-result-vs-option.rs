use std::fs::File;
use std::io;
use std::collections::HashMap;

fn main(){
	let mut a = String::new();
	let result_example = io::stdin().read_line(&mut a);
	match result_example {
		Ok(_) => println!("read_line success"),
		Err(_) => println!("read_line error")
	}

	let mut b = HashMap::new();
	b.insert("foo".to_string(), 10);
	let option_example = b.get(&"foo".to_string());
	match option_example {
		Some(x) => println!("got {x}"),
		None => println!("got nothing")
	}
}
