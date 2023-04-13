use rand::Rng;
use std::io;

fn main() {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("msg");
    a = String::from(a.strip_suffix("\n").expect("msg"));
    let b: String = rand::thread_rng().gen_range(1..10).to_string();
    if a == b {
        println!("correct");
    } else {
        println!("incorrect");
    }
    println!("{a} {b}");
}
