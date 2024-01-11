use proconio::input;

fn main() {
    input! {
        n: i32,
    }
    for x2 in 0..=n {
        for y2 in 0..=n {
            for z2 in 0..=n {
                if x2 + y2 + z2 <= n {
                    println!("{} {} {}", x2, y2, z2);
                }
            }
        }
    }
}
