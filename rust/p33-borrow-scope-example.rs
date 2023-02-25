fn main(){
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
        let val = r1.len();
        println!("{val}")
    }
    let r2 = &mut s;
    let val = r2.len();
    println!("{s} {val}");
}