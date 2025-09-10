use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        ss: [String; n],
    }

    let mut ans = vec![0; n];

    for i in 0..m {
        let mut cnt0 = 0;
        let mut cnt1 = 0;

        for s in ss.iter() {
            let c = s.chars().nth(i).unwrap();
            if c == '0' {
                cnt0 += 1;
            } else {
                cnt1 += 1;
            }
        }

        if cnt1 > cnt0 {
            for j in 0..n {
                if ss[j].chars().nth(i).unwrap() == '0' {
                    ans[j] += 1;
                }
            }
        } else if cnt0 > cnt1 {
            for j in 0..n {
                if ss[j].chars().nth(i).unwrap() == '1' {
                    ans[j] += 1;
                }
            }
        } else {
            for v in ans.iter_mut() {
                *v += 1
            }
        }
    }

    let max_v = *ans.iter().max().unwrap();
    let mut res = Vec::new();
    for (i, v) in ans.iter().enumerate() {
        if *v == max_v {
            res.push((i+1).to_string())
        }
    }

    println!("{}", res.join(" "));
}
