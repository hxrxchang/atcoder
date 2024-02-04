use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut ans: i64 = 0;

    for a2 in a {
        ans += a2;
        if ans < 0 {
            ans = 0;
        }
    }

    println!("{}", ans)
}
