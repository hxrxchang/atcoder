import math

S = list(input())
maxi = math.ceil(math.log2(10 ** 100))

# dp[i][j]: 最初にjにいた子どもが 2 ** i 回目に移動したときにいる場所
dp = [[i for i in range(len(S))] for _ in range(maxi)]

for i, s in enumerate(S):
  dp[0][i] = i + 1 if s == 'R' else i - 1

for i in range(1, maxi):
  for j in range(len(S)):
    dp[i][j] = dp[i - 1][dp[i - 1][j]]

ans = [0] * len(S)
for i in dp[-1]:
  ans[i] += 1

print(*ans)
