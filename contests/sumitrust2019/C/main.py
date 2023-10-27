X = int(input())

dp = [False] * (X + 1)
dp[0] = True

items = [100, 101, 102, 103, 104, 105]
for i in range(1, X + 1):
  for item in items:
    idx = i - item
    if idx >= 0 and dp[idx]:
      dp[i] = True
      break

if dp[X]:
  print(1)
else:
  print(0)
