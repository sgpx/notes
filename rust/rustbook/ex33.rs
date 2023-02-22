fn main() {
    let mut i = 0;
    let a = [1, 2, 3, 4];

    while i < a.len() {
        let val = a[i];
        println!("{val}");
        i += 1;
    }
}
