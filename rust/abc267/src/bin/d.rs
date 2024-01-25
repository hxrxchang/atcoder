use proconio::input;
use std::cmp;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [i64; n],
    }

    let mut dp = vec![vec![-1e18 as i64; n + 1]; n + 1];
    dp[0][0] = 0;

    for i in 1..=n {
        for j in 0..=n {
            if j == 0 {
                dp[i][j] = 0;
            } else if i >= j {
                dp[i][j] = cmp::max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] * j as i64);
            }
        }
    }

    println!("{}", dp[n][m]);
}
