use std::io;

fn main() {
    let mut number: String = String::new();
    io::stdin().read_line(&mut number).expect("fail");
    let number: i32 = number.trim().parse().expect("f2");

    if number % 2 == 0 {
        println!("number is even");
    } else {
        println!("number is odd");
    }
}
