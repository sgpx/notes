fn area(dimensions: (i32, i32)) -> i32 {
    dimensions.0 * dimensions.1
}

fn main() {
    let a = (10, 20);
    let b = area(a);

    println!("{}", b);
}
