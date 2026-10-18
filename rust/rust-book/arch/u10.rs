// use std::io;
use rand::Rng;

fn main() {
    let a: i32 = 5;
    let b: i32 = rand::thread_rng().gen_range(1..10).into();
    println!("{a} {b} ");
}
