fn takes_ownership(s: String) {
    println!("{}", s);
}

fn main() {
    let s = String::from("hello");
    takes_ownership(s);
    // println!("{}", s); // does not work because of ownership taken over by function
}
