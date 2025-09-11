use std::collections::HashMap;

use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [i32; n],
        b: [i32; m],
    }

    let mut cnt_a = HashMap::new();
    for v in a {
        *cnt_a.entry(v).or_insert(0) += 1;
    }

    for v in b {
        if let Some(count) = cnt_a.get_mut(&v) {
            *count -= 1;
            if *count == 0 {
                cnt_a.remove(&v);
            }
        }
    }

    let mut res = Vec::new();
    for (k, v) in &cnt_a {
        for _ in 0..*v {
            res.push(k);
        }
    }
    res.sort();

    let ans = res.iter().join(" ");
    println!("{ans}")
}
