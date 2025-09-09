use proconio::input;

fn main() {
    input! {
        s: String
    }
    let chars: Vec<char> = s.chars().collect();
    let a = chars[0].to_digit(10).unwrap();
    let b = chars[2].to_digit(10).unwrap();

    if b == 8 {
        println!("{}-{}", a+1, 1)
    } else {
        println!("{}-{}", a, b+1)
    }
}
