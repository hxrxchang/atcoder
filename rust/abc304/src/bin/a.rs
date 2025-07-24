use proconio::input;

fn main() {
    input! {
        n: usize,
        people: [(String, i64); n]
    }

    let min_idx = people.iter().enumerate().min_by_key(|&(_, (_, age))| age).map(|(i, _)| i).unwrap();

    for i in 0..n {
        let idx = (min_idx + i) % n;
        let name = &people[idx].0;
        println!("{}", *name);
    }
}
