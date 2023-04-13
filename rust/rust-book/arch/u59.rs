enum IpAddrKind {
    V4,
    V6,
}

struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

fn get_ip_type(addr: &IpAddr) -> &'static str {
    if matches!(addr.kind, IpAddrKind::V4) {
        return "v4";
    } else {
        return "v6";
    }
}

fn main() {
    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let work = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::0"),
    };

    println!("{} {}", home.address, get_ip_type(&home));
    println!("{} {}", work.address, get_ip_type(&work));
}
