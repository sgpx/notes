fn gives_ownership() -> String {
    let some_string = String::from("yours");

    some_string
}

fn takes_and_gives_back(a_string: String) -> String {
    a_string
}

fn main() {
    let s1 = gives_ownership();

    let s2 = String::from("hello");
    // s2 is no longer valid

    let s3 = takes_and_gives_back(s2);

    // println!("{} {} {}", s1, s2, s3); // fails because s2 was borrowed after move
    println!("{} {}", s1, s3);
}
