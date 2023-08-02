N = int(input())
dishes = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][0] -> i番目までの皿の中から選んで、お腹を壊していない状態での、美味しさの最大値
# dp[i][1] -> i番目までの皿の中から選んで、お腹を壊した状態での、美味しさの最大値
dp = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
  dish = dishes[i - 1]
  if dish[0] == 0:
    dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][0], dp[i - 1][1]) + dish[1])
  else:
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + dish[1])
  dp[i][0] = max(dp[i - 1][0], dp[i][0])
  dp[i][1] = max(dp[i - 1][1], dp[i][1])

print(max(dp[N]))
