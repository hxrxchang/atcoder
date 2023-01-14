W = int(input())
N, K = map(int, input().split())
screen_shots = []
for _ in range(N):
  width, importance = map(int, input().split())
  screen_shots.append((width, importance))

dp = []
for _ in range(N + 1):
  n = []
  for _ in range(K + 1):
    k = [0] * (W + 1)
    n.append(k)
  dp.append(n)

for n in range(1, N + 1):
  item = screen_shots[n - 1]
  width, importance = item[0], item[1]
  for k in range(1, K + 1):
    for w in range(W + 1):
      if w >= width:
        dp[n][k][w] = max(dp[n - 1][k][w], dp[n - 1][k - 1][w], dp[n - 1][k - 1][w - width] + importance)
      else:
        dp[n][k][w] = max(dp[n - 1][k][w], dp[n - 1][k - 1][w])

print(dp[N][K][W])


