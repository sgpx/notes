fn main() {
    let mut s1 = String::from("hello");
    let a = &mut s1;
    //let b = &mut s1; // second mutable borrow is not allowed

    //println!("{} {}", a, b);
    println!("{}", a);
}
