use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        s: String,
    }
    let mp = HashMap::from([
        ("red", "SSS"),
        ("blue", "FFF"),
        ("green", "MMM")
    ]);

    let ans = *mp.get(s.as_str()).unwrap_or(&"Unknown");
    println!("{ans}");
}
