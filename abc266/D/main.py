N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
max_T = S[-1][0]
# dp[i][j] -> 単位時間i経過時に座標jにいるときの最大値
dp = [[0] * 5 for _ in range(max_T + 1)]

# S2[i][j] -> 単位時間i経過後に座標jにいるとき捕まえられるすぬけくんの大きさ
S2 = [[0] * 5 for _ in range(max_T + 1)]
for s in S:
  S2[s[0]][s[1]] = s[2]

for i in range(1, max_T + 1):
  for j in range(5):
    if i < j:
      continue
    dp[i][j] = max(dp[i - 1][max(0, j - 1)], dp[i - 1][j], dp[i - 1][min(j + 1, 4)])
    dp[i][j] += S2[i][j]

print(max(dp[-1]))
