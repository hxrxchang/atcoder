use proconio::input;

fn main() {
    input! {
        x: i32,
        y: i32,
    }
    let ans = (x + y) % 12;
    if ans == 0 {
        println!("12");
    } else {
        println!("{ans}");
    }
}
