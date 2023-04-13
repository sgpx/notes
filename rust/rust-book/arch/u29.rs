fn main() {
    let x = String::from("lol");
    let y = x;
    // println!("{} {}", y, x); value borrow after move error
    println!("{}", y);
}
