fn main() {
    // let x = {
    //     let mut y = 5;
    //     y + 1; // value with semicolon is NOT block return value
    //     y + 1 // value without semicolon is block return value
    // };

    let x = {
        let y = 5;
        y + 1 // value without semicolon is block return value
    };
    println!(" {x}");
}
