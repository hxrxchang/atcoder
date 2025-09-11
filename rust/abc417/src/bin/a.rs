use proconio::input;

fn main() {
    input! {
        n: usize,
        a: usize,
        b: usize,
        s: String,
    }
    let ans = &s[a..n-b];
    println!("{ans}");
}
