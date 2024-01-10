use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: f32,
        b: f32,
    }
    if b == 1.0 {
        println!("0");
        return;
    }
    let mut cnt = 1;
    let mut num = a;
    while num < b {
        num += a - 1.0;
        cnt += 1;
    }
    println!("{}", cnt);
}
