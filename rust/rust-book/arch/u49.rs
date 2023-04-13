struct Rectangle {
    width: u32,
    height: u32,
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

fn main() {
    let a = Rectangle {
        width: 20,
        height: 30,
    };

    let b = area(&a);

    println!("{}", b);
}
