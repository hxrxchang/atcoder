N = int(input())
T = list(map(int, input().split()))
sum_T = sum(T)

# dp[i][j]: i番目までの料理で時間jを作れるか
dp = [[False] * (sum_T + 1) for i in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  current = T[i - 1]
  for j in range(sum_T + 1):
    if dp[i - 1][j] or (j - current >= 0 and dp[i - 1][j - current]):
      dp[i][j] = True

# 全種類作った状態で、最小の時間を求める
start = sum_T - sum_T // 2
for i in range(start, sum_T + 1):
  if dp[N][i]:
    print(i)
    exit()
