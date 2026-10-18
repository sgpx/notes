// fn main(){
//     let s1 = String::from("hello");
//     let (s2, len) = (s1, s1.len());
//     println!("{s2} {len}");
// }

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("{s1} {len}");
}
