use rand::Rng;
use std::{cmp::Ordering, io};

fn main() {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("msg");
    a = String::from(a.strip_suffix("\n").expect("msg"));
    let b: i32 = a.trim().parse().expect("msg");
    let c: i32 = rand::thread_rng().gen_range(1..10);
    match b.cmp(&c) {
        Ordering::Equal => println!("OK"),
        Ordering::Less => println!("less"),
        Ordering::Greater => println!("more"),
    }
}
