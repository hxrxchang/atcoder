fn main() {
    proconio::input! {
        B: i32,
        G: i32,
    }
    if B > G {
        println!("Bat");
    } else {
        println!("Glove");
    }
}
