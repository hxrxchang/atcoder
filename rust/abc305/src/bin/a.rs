use proconio::input;

fn main() {
    input! {
        n: i64,
    }

    let ans = (5..=100).step_by(5).fold(0, |best, current| {
        if (current - n).abs() < (best - n).abs() {
            current
        } else {
            best
        }
    });

    println!("{ans}");
}
