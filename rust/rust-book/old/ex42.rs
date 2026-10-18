fn change(s : &mut String){
    s.push_str(", world");
}

// fn change(s : &String){
//     s.push_str("abc");
// }

fn main() {
    let mut s1 = String::from("hello");
    change(&mut s1);
    println!("{s1}");
}
