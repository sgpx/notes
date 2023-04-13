fn main() {
    let y: i32 = {
        let x: i32 = 5;
        x + 1
    };
    if y == 7 {
        println!("7");
    } else if y == 8 {
        println!("8");
    } else {
        println!("else {y}");
    }
}
