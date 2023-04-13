use std::io;

fn main() {
    println!("Guess the number");

    println!("input guess: ");

    let mut guess: String = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("failed to read line");

    println!("you guessed {guess}");
}
