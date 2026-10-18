fn main(){
    {
        let s1 = String::from("foobar");
        // let s2 = s1; // gives a borrow 
        let s2 = s1.clone();
        println!("{s1} {s2}")
    }
}