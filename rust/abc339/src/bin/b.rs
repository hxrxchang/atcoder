use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        n: i32,
    }

    let mut grid = vec![vec!['.'; w]; h];
    let mut direction = "right";
    let mut tmp = (0, 1);
    grid[0][0] = '#';

    for _ in 0..n-1 {
        let (h, w) = tmp;
        match direction {
            "right" => {
                if grid[h][w] == '.' {
                    grid[h][w] = '#';
                    direction = "down";
                    tmp = (h + 1, w);
                } else {
                    grid[h][w] = '.';
                    direction = "up";
                    tmp = (h - 1, w);
                }
            },
            "down" => {
                if grid[h][w] == '.' {
                    grid[h][w] = '#';
                    direction = "left";
                    tmp = (h, w - 1);
                } else {
                    grid[h][w] = '.';
                    direction = "right";
                    tmp = (h, w + 1);
                }
            },
            "left" => {
                if grid[h][w] == '.' {
                    grid[h][w] = '#';
                    direction = "up";
                    tmp = (h - 1, w);
                } else {
                    grid[h][w] = '.';
                    direction = "down";
                    tmp = (h + 1, w);
                }
            },
            "up" => {
                if grid[h][w] == '.' {
                    grid[h][w] = '#';
                    direction = "right";
                    tmp = (h, w + 1);
                } else {
                    grid[h][w] = '.';
                    direction = "left";
                    tmp = (h, w - 1);
                }
            },
            _ => {}
        }
    }


    for row in grid.iter() {
        println!("{}", row.iter().collect::<String>());
    }
}
