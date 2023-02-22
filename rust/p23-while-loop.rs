fn main(){
    let mut i = 0; 
    let mut j = 16;
    while i != j {
        i += 2;
        j -= 2;
        println!("{i} {j}");
    }
}