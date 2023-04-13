fn main(){
    let tup: (u64, u64, u64) = (500,102,1);
    let (_x,y,_z)  = tup;

    print!("{y}")
}