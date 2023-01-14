N, W = map(int, input().split())
items = []
for _ in range(N):
  w, v = map(int, input().split())
  items.append((w, v))
INF = 10 ** 10

# 1次元目: 商品の種類
# 2次元目: 価値の大きさ
# 値: 2次元目の値になるかつ重さが最小になるように商品を選んだ際の重さ
dp = []
# 制約 1 <= N <= 100, 1 <= v <= 10**3 のため
max_value = 100 * (10 ** 3) + 1
for i in range(N + 1):
  row = [INF] * max_value
  dp.append(row)

# ここが肝。これがないと値がずっとINFになってしまう。
dp[0][0] = 0

for i in range(N):
  item = items[i]
  weight = item[0]
  value = item[1]
  for j in range(max_value):
    if j >= value:
      dp[i + 1][j] = min(dp[i][j - value] + weight, dp[i][j])
    else:
      dp[i + 1][j] = dp[i][j]

ans = max_value - 1
while(dp[N][ans] > W and ans >= 0):
  ans -= 1

print(ans)
