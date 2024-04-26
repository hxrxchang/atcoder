A, B, C = map(int, input().split())

dp = [[[0.0] * 101 for _ in range(101)] for _ in range(101)]


for a in range(99, A-1, -1):
    for b in range(99, B-1, -1):
        for c in range(99, C-1, -1):
            total = a + b + c
            if total == 0:
                continue
            if a < 100:
                dp[a][b][c] += (a / total) * (dp[a + 1][b][c] + 1)
            if b < 100:
                dp[a][b][c] += (b / total) * (dp[a][b + 1][c] + 1)
            if c < 100:
                dp[a][b][c] += (c / total) * (dp[a][b][c + 1] + 1)

print(dp[A][B][C])
