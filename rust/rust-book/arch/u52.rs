struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let a = Rectangle {
        width: 20,
        height: 30,
    };
    let x = a.area();
    println!("{}", x);
}
