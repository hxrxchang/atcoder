N = int(input())
activities = [list(map(int, input().split())) for _ in range(N)]

dp = [[None] * 3 for _ in range(N)]
for i, a in enumerate(activities[0]):
  dp[0][i] = a

for i in range(1, N):
  dp[i][0] = max(dp[i - 1][1] + activities[i][0], dp[i - 1][2] + activities[i][0])
  dp[i][1] = max(dp[i - 1][0] + activities[i][1], dp[i - 1][2] + activities[i][1])
  dp[i][2] = max(dp[i - 1][0] + activities[i][2], dp[i - 1][1] + activities[i][2])

ans = max(dp[-1])

print(ans)

