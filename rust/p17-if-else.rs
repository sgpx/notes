use std::io;

fn main() {
    let mut number: String = String::new();
    io::stdin().read_line(&mut number).expect("fail");
    let number: i32 = number.trim().parse().expect("f2");

    if number < 10 {
        println!("number less than 10")
    } else if number == 10 {
        println!("number equal to 10");
    } else {
        println!("number greater than 10");
    }
}
