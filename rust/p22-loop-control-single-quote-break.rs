fn main() {
    let mut ctr = 0;

    'outerloop: loop {
        loop {
            ctr += 10;

            print!("ctr : {ctr}\n");
            if ctr == 200 {
                break 'outerloop;
            }
            if ctr % 50 == 0 {
                break;
            }

        }
        ctr += 10;
    }
}
