// use std::io;
// use rand::Rng;
// use core::ops::Range;

fn check_range( a: i32, b: i32, c : i32) -> bool {
   return (a..b).contains(&c);
}

fn main(){

    let r1 = 1..5;
    let x: u32 = 5;
    let res : bool = r1.contains(&x);
    print!("{res}");

    let res2 : bool = check_range(5, 10, 3);
    print!("{res2}");
}