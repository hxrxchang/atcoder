use proconio::input;
use std::cmp;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [i64; n],
    }

    // dp[i][j]: A[i]までの要素の中から、j個選んだ時の最大値
    let mut dp = vec![vec![-1e18 as i64; m + 1]; n + 1];
    dp[0][0] = 0;

    for i in 1..=n {
        for j in 0..=m {
            if j == 0 {
                dp[i][j] = 0;
            } else if i >= j {
                dp[i][j] = cmp::max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] * j as i64);
            }
        }
    }

    println!("{}", dp[n][m]);
}
