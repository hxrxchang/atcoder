use proconio::input;

fn main() {
    input! {
        h: i32,
        w: i32,
        n: i32,
    }
    let mut grid = vec![vec!['.'; w as usize]; h as usize];
    let mut current_h: i32 = 0;
    let mut current_w: i32 = 0;
    // 0: up, 1: right, 2: down, 3: left
    let mut direction = 0;

    for _ in 0..n {
        if grid[current_h as usize][current_w as usize] == '.' {
            grid[current_h as usize][current_w as usize] = '#';
            direction += 1;
        } else {
            grid[current_h as usize][current_w as usize] = '.';
            direction -= 1;
        }
        direction %= 4;
        if direction < 0 {
            direction += 4;
        }

        match direction {
            0 => {
                current_h -= 1;
            }
            1 => {
                current_w += 1;
            }
            2 => {
                current_h += 1;
            }
            3 => {
                current_w -= 1;
            }
            _ => {
                unreachable!();
            }
        }
        current_h %= h;
        if current_h < 0 {
            current_h += h;
        }
        current_w %= w;
        if current_w < 0 {
            current_w += w;
        }
    }

    for row in grid {
        println!("{}", row.iter().collect::<String>());
    }
}
