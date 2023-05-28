INF = 10**18

X, Y, Z = map(int, input().split())
S = input()

dp = [[INF] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0

for i in range(len(S)):
  cur = 0 if S[i] == 'a' else 1
  for j in range(2):
    for k in range(2):
      v = dp[i][j]
      if j != k:
        v += Z
      if cur == k:
        v += X
      else:
        v += Y
      dp[i + 1][k] = min(dp[i + 1][k], v)

print(min(dp[len(S)][0], dp[len(S)][1]))
