use proconio::input;

fn main() {
    input! {
        n: i32,
    }
    for i in 1..50000 {
        if (i as f64 * 1.08) as i32 == n {
            println!("{}", i);
            return;
        }
    }
    println!(":(")
}
