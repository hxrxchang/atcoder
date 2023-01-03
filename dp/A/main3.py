N = 10
dp = [None] * (N + 1)

def rec(i):
  if i == 0 or i == 1:
    dp[i] = 1
    return 1
  if dp[i] != None:
    return dp[i]
  dp[i] = rec(i - 1) + rec(i - 2)
  return dp[i]

ans = rec(N)
print(ans)
