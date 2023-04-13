use std::io;

fn mai2n() {
    let mut a: String = String::new();
    io::stdin().read_line(&mut a).expect("Err");
}

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}
