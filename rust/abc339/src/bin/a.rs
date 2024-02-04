use proconio::input;

fn main() {
    input! {
        s: String,
    }
    let parts: Vec<&str> = s.split('.').collect();
    println!("{}", parts.last().unwrap());
}
