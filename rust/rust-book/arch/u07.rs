use std::io;

fn main() {
    let mut a: String = String::new();
    let b = 5;
    io::stdin().read_line(&mut a).expect("Error");
    println!("{a} {}", b + 5);
}
