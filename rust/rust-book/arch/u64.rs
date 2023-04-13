enum Colors {
    Red,
    Blue,
    Green,
}

fn main() {
    let x = Colors::Red;
    let y = match x {
        Colors::Red => 1,
        Colors::Blue => 2,
        Colors::Green => 3,
    };
    println!("{}", y);
}
