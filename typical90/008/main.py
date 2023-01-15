N = int(input())
S = input()

max_n = 100000
dp = []
for _ in range(max_n + 1):
  row = [0] * 8
  dp.append(row)

dp[0][0] = 1
for i in range(N):
  for j in range(8):
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

  for j in range(8):
    dp[i + 1][j] %= 10 ** 9 + 7

print(dp[N][7])

