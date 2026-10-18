struct Point(i32, i32, i32);

fn main() {
    let origin = Point(0, 0, 0);
    println!("{} {} {}", origin.0, origin.1, origin.2);
}
