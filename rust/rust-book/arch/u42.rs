fn main() {
    let s = String::from("hello world\n");
    let len = s.len();

    let slice1 = &s[0..len];
    let slice2 = &s[..];

    println!("{} {}", slice1, slice2);
}
