use std::fs::File;

fn main() {
    let a = File::open("Cargo.toml");
    match a {
        Ok(_) => println!("opened"),
        Err(_) => println!("could not open"),
    }
}
