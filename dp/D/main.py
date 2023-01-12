N, W = map(int, input().split())
items = []
for _ in range(N):
  w, v = map(int, input().split())
  items.append((w, v))

# DPのデータ構造
# 1次元目: 品物の個数
# 2次元目: 重さ(0~W)
# 入るデータは価値
dp = []
for _ in range(N + 1):
  row = [0] * (W + 1)
  dp.append(row)

# 0からN個までの品物を1つずつ見ていき、0~Wまでの重さの時点で価値が最大になる品物の組み合わせで得られる価値を保存。
for n in range(N):
  for w in range(W + 1):
    weight = items[n][0]
    value = items[n][1]
    # 品物nが選択可能なとき(nの重さweightが軽い)
    if w >= weight:
      # 選択した方が価値が大きくなるかどうか
      dp[n + 1][w] = max(dp[n][w - weight] + value, dp[n][w])
    else:
      # 品物nが選択不可能
      dp[n + 1][w] = dp[n][w]

print(dp[N][W])
