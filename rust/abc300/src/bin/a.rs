use proconio::input;

fn main() {
    input! {
        (n, a, b): (usize, i64, i64),
        c: [i64; n]
    }

    for (i, v) in c.iter().enumerate() {
        if a + b == *v {
            println!("{}", i+1);
            return;
        }
    }
 }
