use std::io;
use rand::Rng;

fn main(){
    println!("enter number");

    let mut guess: String  = String::new();
    io::stdin().read_line(&mut guess).expect("Failed to read line");
    let secret_number : u32 = rand::thread_rng().gen_range(1..5);
    let gval : u32 = guess.trim().parse().expect("Please type a number");
    println!("number was {secret_number}, guess was {gval}");
}