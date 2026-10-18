fn calculate_length(s: String) -> (String, usize) {
    let v: usize = s.len();
    (s,v)
}

fn main() {
    let s1 = String::from("hello");
    let (s2, len) = calculate_length(s1);
    println!("length of {s2} is {len}");
}
