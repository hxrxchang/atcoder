use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        h: usize,
        w: usize,
        grid: [Chars; h],
    }

    let mut max_length = -1;

    for i in 0..h {
        for j in 0..w {
            if grid[i][j] == '.' {
                let mut visited = vec![vec![false; w]; h];
                visited[i][j] = true;
                dfs((i, j), (i, j), 0, &mut max_length, &grid, &mut visited);
            }
        }
    }

    println!("{}", max_length);
}

fn dfs(start: (usize, usize), now: (usize, usize), count: i32, max_length: &mut i32, grid: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) {
    let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];

    for &(dx, dy) in directions.iter() {
        let nx = (now.0 as i32 + dx) as usize;
        let ny = (now.1 as i32 + dy) as usize;

        if nx < grid.len() && ny < grid[0].len() && grid[nx][ny] == '.' {
            if start == (nx, ny) && count > 1 {
                *max_length = (*max_length).max(count + 1);
            } else if !visited[nx][ny] {
                visited[nx][ny] = true;
                dfs(start, (nx, ny), count + 1, max_length, grid, visited);
                visited[nx][ny] = false;
            }
        }
    }
}
