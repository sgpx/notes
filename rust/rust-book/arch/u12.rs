use rand::Rng;
use std::io;

fn main() {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("error");
    a = String::from(a.strip_suffix("\n").expect("msg"));
    let b: i32 = rand::thread_rng().gen_range(1..=10);
    let c: String = b.to_string();
    if a == c {
        println!("ok");
    }
    println!("{a}#{c}");
}
