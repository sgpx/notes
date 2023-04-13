#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let a = Rectangle {
        width: 20,
        height: 30,
    };

    println!("{:?}", a);
}
