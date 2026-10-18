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

    let mut ms2 = MyStruct {
        a: 3,
        b: 4,
        c: String::from(""),
    };
    ms2.c = String::from("hey");

    println!("{} {}", ms1.a, ms2.b);
}
