fn takes_and_gives_back(s: String) -> String {
    s
}

fn main() {
    let s1 = gives_ownership();
    println!("{s1}");
    let s2 = String::from("hello");
    let s3 = takes_and_gives_back(s2);
    println!("{s3}");
}

fn gives_ownership() -> String {
    let r = String::from("ok");
    r
}
