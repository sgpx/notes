fn change_str(some_string: &mut String) {
    some_string.push_str(", world");
}

fn main() {
    let mut s1 = String::from("hello");
    change_str(&mut s1);
    println!("{}", s1);
}
