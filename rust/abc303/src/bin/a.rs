use proconio::input;

fn main() {
    input! {
        _: usize,
        s: String,
        t: String,
    }

    for (sc, tc) in s.chars().zip(t.chars()) {
        if !is_similar(sc, tc) {
            println!("No");
            return;
        }
    }
    println!("Yes")
}

fn is_similar(a: char, b: char) -> bool {
    if a == b || (a == '1' && b == 'l') || (a == 'l' && b == '1') || (a == '0' && b == 'o') || (a == 'o' && b == '0') {
        return true;
    }
    false
}
