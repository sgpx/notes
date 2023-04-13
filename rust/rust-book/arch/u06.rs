use std::io;

fn main() {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("Err");
    println!("{a}");
}
