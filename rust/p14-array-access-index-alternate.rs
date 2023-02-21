use std::io;

fn main() {
    // radix must respond to
    let a = [1, 2, 3, 4, 5];
    let mut index = String::new();
    io::stdin()
        .read_line(&mut index)
        .expect("failed to read line");
    let b: usize = index.trim().parse().expect("fail");
    let c = a.get(b).expect("fail2");
    println!("{c}");
}
