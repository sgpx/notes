fn odd_only(x: i32) -> Option<i32> {
    if x % 2 == 1 {
        Some(x)
    } else {
        None
    }
}

fn main() {
    let a = odd_only(5);
    match a {
        Some(i) => println!("odd number : {}", i),
        None => println!("even number"),
    }
}
