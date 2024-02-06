use im_rc::HashMap;
use proconio::{input, marker::Chars};

fn main() {
    input! {
        s: Chars,
        n: i64,
    }
    let mut bit_to_int_map = HashMap::new();
    for i in 1..=60 {
        let base: i64 = 2;
        bit_to_int_map.entry(i).or_insert(base.pow(i - 1));
    }

    let mut cnt: i64 = 0;

    for (i, c) in s.iter().enumerate() {
        let j = (s.len() - i) as u32;
        if *c == '1' {
            cnt += bit_to_int_map[&j];
        }
    }

    if cnt > n {
        println!("-1");
        return;
    }

    for (i, c) in s.iter().enumerate() {
        if *c == '?' {
            let j = (s.len() - i) as u32;
            if cnt + bit_to_int_map[&j] <= n {
                cnt += bit_to_int_map[&j];
            }
        }
    }

    println!("{}", cnt);
}
