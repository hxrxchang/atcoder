S = input()
N = len(S)
MOD = 998244353

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if S[i] != ')':
      dp[i + 1][j + 1] = dp[i][j]
      dp[i + 1][j + 1] %= MOD
    if j != 0 and S[i] != '(':
      dp[i + 1][j - 1] += dp[i][j]
      dp[i + 1][j - 1] %= MOD

print(dp[N][0])
