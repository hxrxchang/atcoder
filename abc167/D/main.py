import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

maxi = math.ceil(math.log2(K))

dp = [[0] * N for _ in range(maxi)]

for i, a in enumerate(A):
  dp[0][i] = a

for i in range(1, maxi):
  for j in range(N):
    dp[i][j] = dp[i - 1][dp[i - 1][j]]

position = 0
for i in range(maxi, -1, -1):
  if (K >> i) & 1:
    position = dp[i][position]

print(position + 1)
