use std::io;

fn main() {
    let mut number: String = String::new();
    io::stdin().read_line(&mut number).expect("fail");
    let number: i32 = number.trim().parse().expect("f2");

    let output : String = if number % 2 == 0 { "even".to_string() } else { "odd".to_string() };
    println!("{output}");
}
