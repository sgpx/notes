#[derive(PartialEq)]
enum IpAddrKind {
    V4,
    V6,
}

/*
fn route(ip_kind : IpAddrKind) {

}
*/
struct IpAddr {
    kind: IpAddrKind,
    address: String,
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

    let z = if home.kind == IpAddrKind::V4 {
        "v4"
    } else {
        "v6"
    };

    println!("{} {}", home.address, z);
    println!("{} {}", work.address, z);
}
