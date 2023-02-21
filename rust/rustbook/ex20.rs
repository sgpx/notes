fn print_labeled_measurements(value: i32, unit_label: char) {
    println!("measurement is {value}{unit_label}");
}

fn main() {
    print_labeled_measurements(5, 'h');
}
