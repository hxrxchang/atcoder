use std::{cmp::Reverse, collections::BinaryHeap};

use proconio::input;

fn main() {
    input! {
        q: usize,
    }

    let mut pq = BinaryHeap::new();

    for _ in 0..q {
        input! {t: i32}
        match t {
            1 => {
                input!{x: i32}
                pq.push(Reverse(x));
            },
            2 => {
                let v = pq.pop().unwrap().0;
                println!("{v}");
            },
            _ => unreachable!(),
        }
   }
}
