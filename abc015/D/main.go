package main

import (
	"fmt"
)

func main() {
    var W int
    fmt.Scan(&W)

    var N, K int
    fmt.Scan(&N, &K)

    screenShots := make([][2]int, N)
    for i := 0; i < N; i++ {
        fmt.Scan(&screenShots[i][0], &screenShots[i][1])
    }

    // dp[n][k][w]:=n番目以下の荷物から k個以下選び、重さwがWを超えないように荷物を選んだ時の価値の最大値
    dp := make([][][]int, N+1)
    for i := range dp {
        dp[i] = make([][]int, K+1)
        for j := range dp[i] {
            dp[i][j] = make([]int, W+1)
        }
    }

    for n := 1; n <= N; n++ {
        width, importance := screenShots[n-1][0], screenShots[n-1][1]
        for k := 1; k <= K; k++ {
            for w := 1; w <= W; w++ {
                if w >= width {
                    dp[n][k][w] = max(dp[n-1][k][w], dp[n-1][k-1][w], dp[n-1][k-1][w-width]+importance)
                } else {
                    dp[n][k][w] = max(dp[n-1][k][w], dp[n-1][k-1][w], 0)
                }
            }
        }
    }

    fmt.Println(dp[N][K][W])
}

func max(x, y, z int) int {
    if x > y {
        if x > z {
            return x
        }
    } else if y > z {
        return y
    }
    return z
}
