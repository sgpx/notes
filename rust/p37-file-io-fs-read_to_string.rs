use std::path::Path;
fn main() {
    let args : Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        println!("not enough args");
        std::process::exit(0);
    }
    let al: usize = args.len();
    let filename : &String = &args[al - 1];

    let path: &Path = Path::new(filename);
    let s : String = std::fs::read_to_string(&path).expect("failed to open file");

    println!("{}", s);
}