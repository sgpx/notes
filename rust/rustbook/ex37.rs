fn take_ownership(s : String){
    println!("took ownership of : {s}");
}

fn main(){
    let a : String = String::from("abc");
    take_ownership(a);
    // throws borrow error
    // println!("{a}"); 

}