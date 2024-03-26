N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
M = 3001

# dp[i][j]: Cのi番目までの数列で、Cのi番目がjであるパターン数
dp = [[0] * M for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    a = A[i]
    b = B[i]
    s = sum(dp[i][:a]) % MOD
    for c in range(a, b + 1):
        s += dp[i][c]
        s %= MOD
        dp[i + 1][c] = s

print(sum(dp[N]) % MOD)
