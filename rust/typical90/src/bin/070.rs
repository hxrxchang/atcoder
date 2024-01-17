use proconio::input;

fn main() {
    input! {
        n: usize,
        points: [(i64, i64); n],
    }

    let mut x: Vec<i64> = points.iter().map(|&(xi, _)| xi).collect();
    let mut y: Vec<i64> = points.iter().map(|&(_, yi)| yi).collect();

    x.sort();
    y.sort();

    let ax = median_low(&x);
    let ay = median_low(&y);

    let ans_x: i64 = x.iter().map(|&xi| (xi - ax).abs()).sum();
    let ans_y: i64 = y.iter().map(|&yi| (yi - ay).abs()).sum();

    println!("{}", ans_x + ans_y);
}

fn median_low(arr: &[i64]) -> i64 {
    let len = arr.len();
    if len % 2 == 0 {
        arr[len / 2 - 1]
    } else {
        arr[len / 2]
    }
}
