extern crate calamine;

use calamine::{open_workbook, Reader, Xlsx};
use std::{collections::HashMap, env};

fn main() {
    let args = env::args().collect::<Vec<String>>();
    let filename = args.last().expect("ERROR: invalid args");
    let mut workbook: Xlsx<_> = open_workbook(filename).expect("ERROR: Cannot open file");

    let mut first_row_passed = false;
    let mut header_map: HashMap<u32, String> = HashMap::new();
    if let Some(Ok(range)) = workbook.worksheet_range("MYSHEET") {
        let required_fields: Vec<&str> = vec![
            "foo",
            "bar",
            "baz",
        ];
        let mut result_vector = vec![];

        for row in range.rows() {
            let row_values: Vec<String> = row.iter().map(|cell| cell.to_string()).collect();
            let rv2 = row_values.clone();
            if first_row_passed == false {
                let mut header_count = 0;
                for item in rv2.iter() {
                    header_map.insert(header_count, String::from(item));
                    header_count += 1;
                }
                first_row_passed = true;
            } else {
                if let Some(first_cell) = row_values.get(0) {
                    let first_cell_string = String::from(first_cell);
                    let mut hv_pair: HashMap<String, String> = HashMap::new();
                    if !first_cell_string.is_empty() {
                        let mut cell_index = 0;
                        for val in row_values.iter() {
                            let header = header_map
                                .get(&cell_index)
                                .expect("ERROR: Some error occurred while getting headers");
                            let header_ref = header.to_string();
                            if required_fields.contains(&&header_ref.as_str()) {
                                hv_pair.insert(header.to_string(), val.to_string());
                            }
                            cell_index += 1;
                        }
                        if hv_pair.len() > 0 {
                            result_vector.push(hv_pair);
                        }
                    }
                }
            }
        }
        let jsout: String =
            serde_json::to_string(&result_vector).expect("ERROR: could not serialize JSON");
        println!("{}", jsout);
    } else {
        println!("ERROR: Sheet named 'MYSHEET' not found.");
    }
}
