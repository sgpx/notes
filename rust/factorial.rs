fn factorial(i : u64) -> u64 {
	if(i == 1) 1;
	else factorial(i-1) * i;
}

fn main(){
	a : u64 = factorial(26);
	println!("{}", a);
}
