use proconio::input;
use std::collections::HashMap;

fn prime_factorize(mut n: u64) -> Vec<u64> {
    let mut factors = vec![];
    while n % 2 == 0 {
        factors.push(2);
        n /= 2;
    }
    let mut f = 3;
    while f * f <= n {
        if n % f == 0 {
            factors.push(f);
            n /= f;
        } else {
            f += 2;
        }
    }
    if n != 1 {
        factors.push(n);
    }
    factors
}

fn how_many(mut n: u64, p: u64) -> u64 {
    let mut res = 0;
    while n % p == 0 {
        n /= p;
        res += 1;
    }
    res
}

fn main() {
    input! {
        k: u64,
    }

    let pf_list = prime_factorize(k);
    let mut pf_dict = HashMap::new();
    for p in pf_list {
        *pf_dict.entry(p).or_insert(0) += 1;
    }

    let mut ans = 0;
    for (&p, &e) in &pf_dict {
        let mut f = 0;
        let mut n = p;
        while f < e {
            f += how_many(n, p);
            if f >= e {
                ans = ans.max(n);
                break;
            }
            n += 1;
        }
    }

    println!("{}", ans);
}
