use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        x: [i32; n],
    }
    let mut ans = std::i32::MAX;
    for p in 1..=100 {
        let mut sum = 0;
        for i in 0..n {
            sum += (x[i] - p).pow(2);
        }
        ans = ans.min(sum);
    }
    println!("{}", ans);
}
