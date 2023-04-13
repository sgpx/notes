struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let a = Rectangle {
        width: 20,
        height: 30,
    };
    let b = Rectangle {
        width: 10,
        height: 30,
    };
    let x = a.area();
    println!("{}", x);
    println!("{}", a.can_hold(&b));
}
