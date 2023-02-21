fn main() {
    // let x = 5;
    let x = 5;
    print!("value of x {x} in outer scope\n");
    {
        let x = 6;
        print!("value of x {x} in inner scope\n");
    }
    print!("value of x {x} in outer scope after inner scope\n");
}
