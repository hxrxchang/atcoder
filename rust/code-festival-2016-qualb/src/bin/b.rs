use proconio::{fastout, input};
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        a: i32,
        b: i32,
        s: Chars,
    }

    let mut all_passed = 0;
    let mut foreigner_passed = 0;

    for c in s {
        match c {
            'a' => {
                if all_passed < a + b {
                    println!("Yes");
                    all_passed += 1;
                } else {
                    println!("No");
                }
            },
            'b' => {
                if all_passed < a + b && foreigner_passed < b {
                    println!("Yes");
                    all_passed += 1;
                    foreigner_passed += 1;
                } else {
                    println!("No");
                }
            },
            'c' => {
                println!("No");
            },
            _ => unreachable!(),
        }
    }
}
