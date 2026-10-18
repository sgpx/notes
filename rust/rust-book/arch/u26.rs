fn main() {
    let s = 5;
    {
        let s = 6;
        println!("{s}");
    }
    println!("{s}");
}
