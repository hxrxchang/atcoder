import math

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

maxi = math.ceil(math.log2(10 ** 9))

dp = [[0] * N for _ in range(maxi)]

for i in range(N):
  dp[0][i] = A[i]

for d in range(1, maxi):
  for i in range(N):
    dp[d][i] = dp[d - 1][dp[d - 1][i]]

for x, y in queries:
  x -= 1
  for d in range(maxi, -1, -1):
    if (y >> d) & 1:
      x = dp[d][x]
  print(x + 1)
