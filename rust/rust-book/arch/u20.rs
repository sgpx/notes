fn main() {
    let mut i: i32 = 1;
    let x: i32 = loop {
        i = i + 1;
        if i > 10 {
            break i * 10;
        }
    };
    println!("x : {x}");
}
