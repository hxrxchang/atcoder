use proconio::input;

fn main() {
    input! {
        _: usize,
        l: usize,
        r: usize,
        s: String,
    }
    let substring: String = s.chars().skip(l-1).take(r - l + 1).collect();
    if substring.contains('x') {
        println!("No");
    } else {
        println!("Yes");
    }
}
