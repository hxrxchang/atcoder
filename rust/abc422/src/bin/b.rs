use proconio::{input, marker::Chars};

fn main() {
    input! {
        h: usize,
        w: usize,
        grid: [Chars; h],
    }

    for y in 0..h {
        for x in 0..w {
            if grid[y][x] == '#' {
                let mut cnt = 0;
                // 上
                if y > 0 && grid[y-1][x] == '#' {
                    cnt += 1;
                }
                // 下
                if y < h-1 && grid[y+1][x] == '#' {
                    cnt += 1;
                }
                // 左
                if x > 0 && grid[y][x-1] == '#' {
                    cnt += 1;
                }
                // 右
                if x < w-1 && grid[y][x+1] == '#' {
                    cnt += 1;
                }
                if !(cnt == 2 || cnt == 4) {
                    println!("No");
                    return;
                }
            }
        }
    }

    println!("Yes")
}
