fn fxn(x: i32) -> Option<i32> {
    if x % 2 == 1 {
        Some(x)
    } else {
        None
    }
}

fn main() {
    let a = fxn(6);
    match a {
        Some(x) => println!("got {}", x),
        None => println!("nothing"),
    }
}
