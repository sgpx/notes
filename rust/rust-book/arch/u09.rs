// use std::io;
use rand::Rng;

fn main() {
    let a = 5;
    let range = rand::thread_rng().gen_range(1..10);
    let b: i32 = range.into();
    println!("{a} {b} ");
}
