fn main() {
    let a: &str = "hello";
    let mut s: String = String::from(a);
    s.push_str(", world");
    println!("{s}");
}
