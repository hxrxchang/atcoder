N, M, K, S, T, X = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
mod = 998244353

# dp[i][j]: i回の移動でjにたどり着く方法の数のうち、dp[i][j][0] = Xを通る回数が偶数、dp[i][j][1] = Xを通る回数が奇数のものの数
dp = [[[0, 0] for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][S][0] = 1

for i in range(1, K + 1):
  for u, v in edges:
    if v == X:
      # 偶奇が入れ替わる
      dp[i][v][0] += dp[i - 1][u][1]
      dp[i][v][1] += dp[i - 1][u][0]
    else:
      dp[i][v][0] += dp[i - 1][u][0]
      dp[i][v][1] += dp[i - 1][u][1]
    dp[i][v][0] %= mod
    dp[i][v][1] %= mod

    if u == X:
      # 偶奇が入れ替わる
      dp[i][u][0] += dp[i - 1][v][1]
      dp[i][u][1] += dp[i - 1][v][0]
    else:
      dp[i][u][0] += dp[i - 1][v][0]
      dp[i][u][1] += dp[i - 1][v][1]
    dp[i][u][0] %= mod
    dp[i][u][1] %= mod

ans = dp[K][T][0]
print(ans)

