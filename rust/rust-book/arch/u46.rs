struct MyStruct {
    a: i32,
    b: u64,
    c: String,
}

fn main() {
    let ms1 = MyStruct {
        a: 1,
        b: 2,
        c: String::from("hello"),
    };

    let mut ms2 = MyStruct { b: 4, ..ms1 };
    ms2.c = String::from("hey");

    println!("{} {}", ms1.a, ms2.b);
}
