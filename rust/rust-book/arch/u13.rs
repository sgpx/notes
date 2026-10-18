fn main() {
    let a: String = String::from("abc");
    let b: Option<&str> = a.strip_suffix("bc");
    let c: &str = b.expect("error");
    println!("{a} {c}");
}
