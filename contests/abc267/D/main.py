n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(m+1):
        if j == 0:
            dp[i][0] = 0
        elif i >= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1] * j)
    # print(dp[i])

print(dp[n][m])
