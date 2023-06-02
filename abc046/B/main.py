N, K = map(int, input().split())

dp = [0] * N
dp[0] = K

for i in range(1, N):
  dp[i] = dp[i-1] * (K - 1)

print(dp[-1])
