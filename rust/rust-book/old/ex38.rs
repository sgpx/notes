fn take_ownership(s : String){
    println!("took ownership of : {s}");
}

fn make_copy(i : i32){
    println!("copy: {i}");
}

fn main(){
    let a : String = String::from("abc");
    take_ownership(a);
    // throws borrow error
    // println!("{a}"); 

    let b : i32 = 5;
    make_copy(b);
    println!("main: {b}");
}