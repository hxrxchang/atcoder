N = int(input())
dishes = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N+1)]  # DPテーブルの初期
for i in range(1, N+1):
  dish = dishes[i-1]
  if dish[0] == 1:
    if i != 0 and dp[i - 1][0] == dp[i - 1][1]:
      dp[i][0] = dp[i-1][0]
      dp[i][1] = dp[i-1][1]
    else:
      dp[i][0] = max(dp[i-1][0] + dish[1], dp[i - 1][0])
      dp[i][1] = dp[i-1][1]
  else:
    dp[i][0] = max(dp[i-1][0] + dish[1], dp[i - 1][0])
    dp[i][1] = max(dp[i-1][1] + dish[1], dp[i - 1][1])

print(dp[-1])
