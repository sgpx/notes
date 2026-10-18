fn main() {
    let mychar : char = 'z';
    let res: u32 = mychar.to_digit(10).expect("could not convert to digit, failed");
    print!("{mychar} {res}\n");
}