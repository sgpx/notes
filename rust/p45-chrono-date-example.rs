use chrono::{DateTime, Days, FixedOffset, ParseResult };

fn parse_date(date_str: &str) -> ParseResult<DateTime<FixedOffset>> {
    return DateTime::parse_from_rfc3339(date_str);
}

fn main() {
    let x = parse_date("2022-01-01T00:00:00+00:00").unwrap();
    let t = Days::new(1);
    let y = x.checked_add_days(t).unwrap();
    println!("{:#?}", y);
}
