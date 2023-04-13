enum IpAddrType {
    IPv4(u8, u8, u8, u8),
    IPv6(String),
}

fn checkAddr(x: IpAddrType) {
    match x {
        IpAddrType::IPv4(x0, x1, x2, x3) => println!("v4, {} {} {} {}", x0, x1, x2, x3),
        IpAddrType::IPv6(s) => println!("v6 {}", s),
    }
}

fn main() {
    let x = IpAddrType::IPv4(1, 2, 3, 4);
    let y = IpAddrType::IPv6(String::from("::0"));

    checkAddr(x);
    checkAddr(y);
}
