N, K = map(int, input().split())

schedule = [0] * (N + 1)
for _ in range(K):
  A, B = map(int, input().split())
  schedule[A] = B

# dp[i][j]: i番目のパスタがj日目に選ばれるパターン数
# i = 1: トマトソース、i = 2: クリームソース,、i = 3: バジルソース
dp = [[0] * (N + 1) for _ in range(4)]
dp[1][0] = 1

for i in range(1, N + 1):
  if schedule[i] != 0:
    for j in range(1, 4):
      dp[schedule[i]][i] += dp[j][i - 1]
    if i - 2 > 0 and dp[schedule[i]][i - 1] > 0 and dp[schedule[i]][i - 2] > 0:
      dp[schedule[i]][i - 1] -= dp[schedule[i]][i - 2]
      dp[schedule[i]][i] -= dp[schedule[i]][i - 2]
  else:
    for j in range(1, 4):
      for k in range(1, 4):
        dp[j][i] += dp[k][i - 1]
    for j in range(1, 4):
      if i - 2 > 0 and dp[j][i - 1] > 0 and dp[j][i - 2] > 0:
        dp[j][i - 1] -= dp[j][i - 2]
        dp[j][i] -= dp[j][i - 2]

ans = 0
for i in range(1, 4):
  ans += dp[i][-1]

print(ans % 10000)
