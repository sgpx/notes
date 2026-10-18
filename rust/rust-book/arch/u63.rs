#[derive(Debug)]
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

fn main() {
    let x = IpAddr::V4(1, 2, 3, 4);
    let y = IpAddr::V6(String::from("::0"));
    println!("{:?}", y);
    let z = if matches!(y, IpAddr::V6(_)) {
        "ok"
    } else {
        "nok"
    };
    println!("{}", z);
}
