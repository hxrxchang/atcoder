use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        a: usize,
        n: usize,
    }

    let mut graph = vec![-1; n * 10];
    let mut que = VecDeque::new();
    graph[1] = 0;
    que.push_back(1);

    while let Some(tmp) = que.pop_front() {
        if tmp > 10 && tmp % 10 != 0 {
            let str_tmp = tmp.to_string();
            let operated = str_tmp[str_tmp.len() - 1..].to_string() + &str_tmp[..str_tmp.len() - 1];
            let operated = operated.parse::<usize>().unwrap();

            if operated < graph.len() && graph[operated] == -1 {
                graph[operated] = graph[tmp] + 1;
                que.push_back(operated);
            }
        }

        if tmp * a < graph.len() && graph[tmp * a] == -1 {
            graph[tmp * a] = graph[tmp] + 1;
            que.push_back(tmp * a);
        }
    }

    println!("{}", graph[n]);
}
