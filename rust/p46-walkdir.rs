use std::fs;
use serde_json::json;
use walkdir::WalkDir;
// use std::fs;
fn main() {
    let mut xc: Vec<String> = vec![];
    let mut yc: Vec<u8> = vec![];
    for entry in WalkDir::new("data") {
        let entry = entry.unwrap();
        let lp = entry.path();
        if lp.is_file() {
            // let ls = lp.display();
            let lx = lp.to_str().expect("msg1");
            let lss = String::from(lx);
            let ispy: u8 = if lss.contains("python") { 1 } else { 0 };
            let content_result: Result<String, std::io::Error> = fs::read_to_string(lp);
            if content_result.is_ok() {
                // println!("{}", ls);
                let content: String = content_result.unwrap();
                let bytes = content.as_bytes().chunks(4096);
                for chunk in bytes {
                    let s = std::str::from_utf8(chunk);
                    if s.is_ok() {
                        let s2 = String::from(s.unwrap());
                        xc.push(s2);
                        yc.push(ispy);
                    }

                    // println!("{}", s2);
                }
            }
        }
    }
    let exported = json!({"Xc": xc, "yc": yc});
    let json_str = exported.to_string();
    fs::write("data.json", json_str).expect("fail")
}
