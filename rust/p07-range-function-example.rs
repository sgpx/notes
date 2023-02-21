fn sum(a: u32, b: u32) -> u32 {
    return a + b;
}

fn check_range(a: i32, b: i32, c: i32) -> bool {
    return (a..b).contains(&c);
}

fn main() {
    let r1 = 1..5;
    let x: u32 = 5;
    let res: bool = r1.contains(&x);
    print!("{res}\n");

    let res2: bool = check_range(5, 10, 3);
    print!("{res2}\n");

    let res3 = sum(1, 1);
    print!("{res3}\n");
}
