N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# dp[i][w]: i番目までの品物から重さがwを超えないように選んだときの価値の総和の最大値
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  for w in range(1, W + 1):
    weight, value = items[i - 1][0], items[i - 1][1]
    if weight > w:
      dp[i][w] = dp[i - 1][w]
    else:
      dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp)
