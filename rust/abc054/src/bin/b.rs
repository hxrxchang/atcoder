use proconio::{fastout, input};
use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        a: [Chars; n],
        b: [Chars; m],
    }
    for i in 0..n - m + 1 {
        for j in 0..n - m + 1 {
            if check(&a, &b, i, j) {
                println!("Yes");
                return;
            }
        }
    }
    println!("No");
}

fn check(a: &Vec<Vec<char>>, b: &Vec<Vec<char>>, si: usize, sj: usize) -> bool {
    for i in 0..b.len() {
        for j in 0..b.len() {
            if a[i + si][j + sj] != b[i][j] {
                return false;
            }
        }
    }
    true
}
