use proconio::input;
use std::{cmp::Reverse, collections::{BinaryHeap, HashMap}};

fn main() {
    input! {
        n: usize,
        slimes: [(i64, i64); n]
    }

    let mut heap = BinaryHeap::new();
    let mut counts = HashMap::new();

    for s in slimes {
        let (slime_name, cnt) = s;
        heap.push(Reverse(slime_name));
        *counts.entry(slime_name).or_insert(0) += cnt;
    }

    while let Some(s) = heap.pop() {
        let slime_name = s.0;
        let slime_cnt = counts.get(&slime_name).unwrap();
        if slime_cnt >= &2 {
            let next_slime_cnt = slime_cnt / 2;
            let next_slime_name: i64 = slime_name * 2;
            heap.push(Reverse(next_slime_name));
            *counts.entry(slime_name).or_insert(0) = slime_cnt % 2;
            *counts.entry(next_slime_name).or_insert(0) += next_slime_cnt;
        }
    }

    let result: i64 = counts.values().sum();
    println!("{}", result);
}
