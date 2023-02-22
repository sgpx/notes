fn fxn(s1 : String){
    println!("{s1}");
}
fn main() {
    let s1 = gives_ownership();
    println!("{s1}");
    fxn(s1);
    println!("{s1}");

}

fn gives_ownership() -> String {
    let r = String::from("ok");
    r
}
