use std::io;

fn main(){
    println!("enter number");

    let mut guess: String  = String::new();
    io::stdin().read_line(&mut guess).expect("Failed to read line");
    println!("number was {guess}");
}