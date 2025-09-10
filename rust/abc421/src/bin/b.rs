use proconio::input;

fn main() {
    input! {
        x: i64,
        y: i64,
    }

    let mut a = Vec::new();
    a.push(x);
    a.push(y);

    for i in 2..10 {
        a.push(f(&a, i));
    }

    println!("{}", a[9])
}

fn f(v: &Vec<i64>, i: usize) -> i64 {
    let x = v[i-1] + v[i-2];
    let s = x.to_string();
    let rev: String = s.chars().rev().collect();
    rev.parse::<i64>().unwrap()
}
