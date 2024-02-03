use proconio::input;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

fn main() {
    input! {
        n: usize,
        k: usize,
        p: [usize; n],
    }

    let mut heap = BinaryHeap::new();

    for &item in &p[0..k] {
        heap.push(Reverse(item));
    }

    let mut item = heap.pop().unwrap();
    println!("{}", item.0);

    for &next_item in &p[k..n] {
        if next_item > item.0 {
            heap.push(Reverse(next_item));
            item = heap.pop().unwrap();
        }
        println!("{}", item.0);
    }
}
