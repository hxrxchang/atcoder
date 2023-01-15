N = int(input())
S = input()
atcoder = "atcoder"

# dp[i][j]: Sのi文字目までを用いた時、文字列"atcoder"のj文字目までを作る通りの数
dp = []
for _ in range(N + 1):
  row = [0] * (len(atcoder) + 1)
  dp.append(row)

dp[0][0] = 1
for i in range(N):
  for j in range(len(atcoder) + 1):
    dp[i + 1][j] += dp[i][j]
    if S[i] == 'a' and j == 0:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 't' and j == 1:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 'c' and j == 2:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 'o' and j == 3:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 'd' and j == 4:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 'e' and j == 5:
      dp[i + 1][j + 1] += dp[i][j]
    if S[i] == 'r' and j == 6:
      dp[i + 1][j + 1] += dp[i][j]

  for j in range(len(atcoder) + 1):
    dp[i + 1][j] %= 10 ** 9 + 7

print(dp[N][len(atcoder)])

