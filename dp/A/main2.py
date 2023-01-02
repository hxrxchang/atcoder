import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
H = list(map(int, input().split()))
INF = 2 ** 60

dp = [-1] * N

def rec(i):
  if i == 0:
    return 0

  if dp[i] != -1:
    return dp[i]

  result = INF

  if i - 1 >= 0:
    result = min(result, rec(i - 1) + abs(H[i] - H[i - 1]))
  if i - 2 >= 0:
    result = min(result, rec(i - 2) + abs(H[i] - H[i - 2]))

  dp[i] = result
  return result

ans = rec(N - 1)
print(ans)
