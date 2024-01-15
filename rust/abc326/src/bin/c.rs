use std::collections::HashMap;

use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; n],
    }

    let mut map: HashMap<usize, usize> = HashMap::new();
    for a2 in &a {
        map.entry(*a2).and_modify(|e| *e += 1).or_insert(1);
    }

    let mut tmp: i32 = 0;
    for i in 1..m {
        if let Some(v) = map.get(&i) {
            tmp += *v as i32;
        }
    }

    let mut ans = &tmp.clone();
    let max = &a.iter().max().unwrap();
    for i in m..**max {
        let drop: &&usize = &map.get(&(i - m)).unwrap_or(&0);
        let add =  &map.get(&i).unwrap_or(&0);
        ans = &ans.max(&tmp);
    }

    panic!("{}", ans)
}
