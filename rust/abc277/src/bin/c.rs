use proconio::input;
use std::collections::{HashMap, VecDeque};

fn main() {
    input! {
        n: usize,
        edges: [(i32, i32); n],
    }

    let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();

    for (a, b) in edges {
        graph.entry(a).or_default().push(b);
        graph.entry(b).or_default().push(a);
    }

    let mut que = VecDeque::new();
    que.push_back(1);
    let mut visited = HashMap::new();
    visited.insert(1, true);

    while let Some(v) = que.pop_front() {
        if let Some(neighbors) = graph.get(&v) {
            for &i in neighbors {
                visited.entry(i).or_insert_with(|| {
                    que.push_back(i);
                    true
                });
            }
        }
    }

    let max_node = visited.keys().max().unwrap_or(&0);
    println!("{}", max_node);
}
