fn main(){
    let mut x= 5;
    let y = loop {
        x += 1;
        if x > 10 { break 20; }
    };
    println!("{x} {y}")

}