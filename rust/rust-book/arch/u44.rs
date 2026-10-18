struct MyStruct {
    a: i32,
    b: u64,
}

fn main() {
    let ms1 = MyStruct { a: 1, b: 2 };

    let ms2 = MyStruct { a: 3, b: 4 };

    println!("{} {}", ms1.a, ms2.b);
}
