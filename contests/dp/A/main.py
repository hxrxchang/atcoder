N = int(input())
H = list(map(int, input().split()))

dp = [None] * N

for i in range(N):
  if i == 0:
    dp[i] = 0
  elif i == 1:
    dp[i] = abs(H[i] - H[i - 1])
  else:
    v1 = dp[i - 1] + abs(H[i - 1] - H[i]) # 1個前の足場からジャンプするとき
    v2 = dp[i - 2] + abs(H[i - 2] - H[i]) # 2個前の足場からジャンプするとき
    dp[i] = min(v1, v2)

print(dp[-1])
