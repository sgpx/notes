fn main() {
    let s = String::from("hello world\n");
    let len = s.len();

    let slice1 = &s[3..len];
    let slice2 = &s[..len];

    println!("{} {}", slice1, slice2);
}
