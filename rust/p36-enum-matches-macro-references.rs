enum IpAddr {
    V4,
    V6,
}


// using references with matches! macro can cause issues and is potentially unsafe

fn check_addr(a: &IpAddr) {
    if matches!(a, IpAddr::V4) {
        println!("ipv4")
    } else {
        println!("ipv6")
    }
}

fn main() {
    let a = IpAddr::V4;
    let b = IpAddr::V6;

    check_addr(&a);
    check_addr(&b);
}
